import requests
from bs4 import BeautifulSoup
import json

def discover_urls(base_url):
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all <a> tags, you might need to adjust the selector for better targeting
    links = soup.find_all('a')
    urls = [link.get('href') for link in links if link.get('href') and link.get('href').startswith('architecture/')]
    # Ensure full URLs
    urls = [f"{base_url}/{url}" if not url.startswith(base_url) else url for url in urls]
    return urls

def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    content_sections = soup.find_all(['h1', 'h2', 'p', 'pre'])
    data = []
    current_section = {"title": None, "content": []}
    for tag in content_sections:
        if tag.name in ['h1', 'h2']:
            if current_section["content"]:
                data.append(current_section)
                current_section = {"title": tag.text.strip(), "content": []}
        else:
            current_section["content"].append(tag.text.strip())
    if current_section["content"]:
        data.append(current_section)
    return data

def save_data(data, filename='data/nearcore_github_io.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def nearcore_github_io():
    base_url = 'https://near.github.io/nearcore'
    urls = discover_urls(base_url)  # Get all URLs from the base page
    all_data = []
    for url in urls:
        page_data = scrape_page(url)
        all_data.extend(page_data)

    save_data(all_data)
    print("Data has been scraped and saved successfully.")
