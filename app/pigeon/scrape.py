import requests
import time
from bs4 import BeautifulSoup
import json
from datetime import datetime
import random


class APNewsScraper:
    def __init__(self):
        self.base_url = "https://apnews.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.session = requests.Session()

    def get_articles(self, max_articles=10):
        """
        Fetches articles from AP News homepage in a respectful manner
        """
        articles = []
        try:
            # Add a random delay between 2-5 seconds before starting
            time.sleep(random.uniform(2, 5))

            response = self.session.get(
                self.base_url, headers=self.headers, timeout=10)
            print(f"Response status code: {response.status_code}")
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            article_links = soup.find_all("a", href=True)

            processed = 0
            for link in article_links:
                if processed >= max_articles:
                    break

                # Only process actual article URLs
                if "/article/" in link["href"] and link["href"].startswith("https"):
                    # Random delay between article processing
                    time.sleep(random.uniform(3, 7))

                    article_data = self._process_article(link["href"])

                    if article_data:
                        articles.append(article_data)
                        processed += 1

        except Exception as e:
            print(f"Error fetching articles: {str(e)}")

        return articles

    def _process_article(self, url):
        """
        Processes a single article page
        """
        print(f"Processing article: {url}")
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract headline
            headline = soup.find("h1.Page-headline")
            headline_text = headline.text.strip() if headline else ""

            # Extract content
            content_div = soup.find("main", {"class": "Page-main"})
            if not content_div:
                raise Exception("Malformed HTML: main content not found")
            paragraphs = content_div.find_all("p")
            content = " ".join([p.text.strip() for p in paragraphs])

            return {
                "url": url,
                "headline": headline_text,
                "content": content,
                "timestamp": datetime.now().isoformat(),
            }

        except Exception as e:
            print(f"Error processing article {url}: {str(e)}")
            return None

    def save_articles(self, articles, filename=None):
        """
        Saves articles to a JSON file with timestamp
        """
        if filename is None:
            filename = f"ap_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)

        return filename


# Usage example
if __name__ == "__main__":
    scraper = APNewsScraper()
    # Limit to 5 articles for testing
    articles = scraper.get_articles(max_articles=5)
    filename = scraper.save_articles(articles)
    print(f"Saved {len(articles)} articles to {filename}")
