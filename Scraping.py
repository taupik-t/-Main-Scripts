import requests
from bs4 import BeautifulSoup

def fetch_web_content(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Return the prettified HTML
            return soup.prettify()
        else:
            return f"Error: Unable to retrieve content. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
url = input("Enter the URL of the website: ")
html_content = fetch_web_content(url)
print(html_content)