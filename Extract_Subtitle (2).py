import ffmpeg
import pysubs2
from googletrans import Translator
import time
import subprocess
import re
import sys

# Define file paths
input_file = 'C:/Users/taupi/Videos/The Amazing World of Gumball/[DLNime.web.id] The Amazing World of Gumball Season 5 Ep 01.mkv'
extracted_subtitle_file = 'extracted_subtitle.srt'
translated_subtitle_file = 'translated_subtitle.srt'
output_file = 'The Amazing World of Gumball Season 5 - Episode 01_with_translated_subtitle.mkv'

print("Starting subtitle extraction...")

# Step 1: Extract existing subtitles from the video
try:
    ffmpeg.input(input_file).output(extracted_subtitle_file, map='0:s:0').run()
    print("Subtitle extraction completed successfully.")
except Exception as e:
    print(f"Error during subtitle extraction: {e}")

time.sleep(10)  # Wait for 10 seconds

print("Starting subtitle translation...")

# Step 2: Translate the extracted subtitles
try:
    # Load the SRT file
    subs = pysubs2.load(extracted_subtitle_file, encoding='utf-8')
    total_subtitles = len(subs)
    
    # Initialize translator
    translator = Translator()

    # Translate each subtitle
    for i, subtitle in enumerate(subs):
        try:
            translated_text = translator.translate(subtitle.text, src='en', dest='id').text
            subtitle.text = translated_text
        except Exception as e:
            print(f"Error translating subtitle {i}: {e}")

        # Print progress every 1%
        if total_subtitles > 0 and i % (total_subtitles // 100) == 0:
            progress_percent = (i + 1) * 100 // total_subtitles
            sys.stdout.write(f"\rTranslation progress: {progress_percent}%")
            sys.stdout.flush()
    
    # Save the translated SRT file
    subs.save(translated_subtitle_file)
    print("\rSubtitle translation completed successfully.        ")
except Exception as e:
    print(f"Error during subtitle translation: {e}")

time.sleep(10)  # Wait for 10 seconds

print("Starting subtitle embedding...")

# Step 3: Add the translated subtitles back to the video alongside the existing subtitles
def progress_callback(line):
    """Callback function to handle FFmpeg progress output."""
    match = re.search(r'time=(\d+:\d+:\d+.\d+)', line)
    if match:
        time_str = match.group(1)
        sys.stdout.write(f"\rEmbedding progress: {time_str}")
        sys.stdout.flush()

try:
    # Run FFmpeg command and capture output
    process = subprocess.Popen(
        [
            'ffmpeg', '-i', input_file, 
            '-i', translated_subtitle_file, 
            '-map', '0', 
            '-map', '1', 
            '-c', 'copy', 
            '-c:s', 'srt', 
            output_file
        ],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    
    # Monitor progress
    last_printed_percentage = 0
    for line in process.stdout:
        progress_callback(line.strip())
        
        # Print progress every 1%
        if 'time=' in line:
            match = re.search(r'time=(\d+):(\d+):(\d+)\.(\d+)', line)
            if match:
                hours, minutes, seconds, milliseconds = map(int, match.groups())
                total_seconds = hours * 3600 + minutes * 60 + seconds
                progress_percent = int((total_seconds / 678) * 100)  # Adjust total seconds as needed

                if progress_percent > last_printed_percentage:
                    sys.stdout.write(f"\rEmbedding progress: {progress_percent}%")
                    sys.stdout.flush()
                    last_printed_percentage = progress_percent
    
    process.wait()  # Wait for the process to finish
    print("\rSubtitle embedding completed successfully.        ")
except Exception as e:
    print(f"Error during subtitle embedding: {e}")

print("All tasks completed.")
