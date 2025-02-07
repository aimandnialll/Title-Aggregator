import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Verge RSS feed URL
URL = "https://www.theverge.com/rss/index.xml"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Function to fetch and parse the RSS feed
def fetch_verge_articles():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return []
    
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")
    articles = []
    
    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text
        
        # Convert pubDate to datetime object
        article_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
        
        # Only include articles from January 1, 2022, onwards
        if article_date.year >= 2022:
            articles.append({"title": title, "link": link, "date": article_date.isoformat()})
    
    return articles

# Fetch articles and save as JSON
def save_articles():
    articles = fetch_verge_articles()
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4)
    print("Articles saved successfully.")

if __name__ == "__main__":
    save_articles()
    
