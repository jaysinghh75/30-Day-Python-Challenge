# Challenge Day 1

# Scrape headlines from a news site

# Import required libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the India Today news page and get the HTML content
html_text_news = requests.get('https://www.indiatoday.in/india').text

# Step 2: Parse the HTML content using BeautifulSoup and lxml parser
soup = BeautifulSoup(html_text_news, 'lxml')

# Step 3: Find all news headlines inside <h2> tags
news = soup.find_all('h2')

# Step 4: Loop through each headline and print the headline and its link
for index, top_news in enumerate(news, 1):
    headline = top_news.a.text  # Extract the text inside the anchor tag (<a>)
    link = top_news.a["href"]   # Extract the URL from the href attribute
    print(f"Headline {index}\n-----------------------------------------------------")
    print(f"{headline}\nFor more info: {link}\n-----------------------------------------------------\n")
