import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Step 1: Send an HTTP request to get the webpage content
url = url = input('Enter the source url(It will only work with urls like https://www.69shu.com/txt/38945/26658057) : ')
parsed_url = urlparse(url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path.rsplit('/', 1)[0]}/"
start_number = int(url.split("/")[-1])
end_number = start_number + int(input('Enter the number of chapters to include (e.g., 50): '))

file_name = input('Enter the name of file (e.g.Sample.txt) : ')

for num in range(start_number, end_number + 1):
    url = f"{base_url}{num}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Step 3: Extract all visible text from the webpage
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span'])

        # Step 4: Write the content to a text file
        with open(file_name, 'a', encoding='utf-8') as file:  # Use 'a' to append to the file
            for tag in paragraphs:
                # Clean up the text by stripping leading/trailing spaces
                text = tag.get_text(strip=True)
                if text:  # Write non-empty text to the file
                    file.write(text + '\n\n')

        print(f"Content from {url} has been written to {file_name}")
    else:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")