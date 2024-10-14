import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Load the HTML content of the page
        html_content = response.text
        
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get the full HTML code
        full_html_code = soup.prettify()

        return full_html_code
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

# URL to scrape
url = "https://yukomik.com/komik/bunking-bed/"  # Replace with your target URL

# Call the function and print the full HTML code
html_code = scrape_website(url)
print(html_code)
