import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://www.eweek.com/artificial-intelligence/ai-companies/"  # Replace with the actual URL you want to scrape

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <h3> tags
    h3_tags = soup.find_all('h3')
    
    # Initialize a counter for numbering the results
    counter = 1
    
    # Iterate through each <h3> tag and find <strong> tags within it
    for h3 in h3_tags:
        strong_tags = h3.find_all('strong')
        
        # Print the text content of each <strong> tag within <h3>
        for tag in strong_tags:
            print(f"{counter}. {tag.text.strip()}")
            counter += 1
    
    # If no results were found, print a message
    if counter == 1:
        print("No <strong> tags found within <h3> tags.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")