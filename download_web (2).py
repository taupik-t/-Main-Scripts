from pywebcopy import save_website
import os

def download_page(url, download_folder):
    # Define the project folder where the website will be copied
    project_folder = os.path.join(download_folder, 'website_download')

    # Make sure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Set the pywebcopy options
    kwargs = {'project_name': 'my_website'}

    # Save the website
    save_website(
        url=url,
        project_folder=project_folder,
        **kwargs
    )
    print(f"Website downloaded to: {project_folder}")

if __name__ == "__main__":
    # Example usage
    url = "https://example.com"  # Replace this with the URL you want to download
    download_folder = "./downloaded_site"  # Replace this with the path to your download folder

    download_page(url, download_folder)
