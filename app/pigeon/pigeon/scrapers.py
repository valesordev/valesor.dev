"""
Base scraper classes and implementations.
"""
import time
import random
import requests
from abc import ABC, abstractmethod
from typing import List, Optional
from bs4 import BeautifulSoup

from .models import Article, Page


class BaseScraper(ABC):
    """Base class for all scrapers."""
    
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/91.0.4472.124 Safari/537.36"
        }
        self.session = requests.Session()
    
    @abstractmethod
    def get_articles(self, max_articles: int = 10) -> List[Article]:
        """Fetch articles from the site."""
        pass
    
    def fetch_page(self, url: str, delay: bool = True) -> Optional[Page]:
        """Fetch a page from the site with optional delay."""
        try:
            if delay:
                time.sleep(random.uniform(2, 5))
                
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            return Page(url=url, html_content=response.text)
        except Exception as e:
            print(f"Error fetching page {url}: {str(e)}")
            return None


class APNewsScraper(BaseScraper):
    """Scraper for AP News."""
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://apnews.com"
    
    def get_articles(self, max_articles: int = 10) -> List[Article]:
        """
        Fetches articles from AP News homepage in a respectful manner.
        """
        articles = []
        try:
            page = self.fetch_page(self.base_url)
            if not page:
                return articles
                
            soup = BeautifulSoup(page.html_content, "html.parser")
            article_links = soup.find_all("a", href=True)
            
            processed = 0
            for link in article_links:
                if processed >= max_articles:
                    break
                    
                if "/article/" in link["href"] and link["href"].startswith("https"):
                    time.sleep(random.uniform(3, 7))
                    
                    article = self._process_article(link["href"])
                    if article:
                        articles.append(article)
                        processed += 1
                        
        except Exception as e:
            print(f"Error fetching articles: {str(e)}")
            
        return articles
    
    def _process_article(self, url: str) -> Optional[Article]:
        """
        Processes a single article page.
        """
        print(f"Processing article: {url}")
        try:
            page = self.fetch_page(url, delay=False)
            if not page:
                return None
                
            soup = BeautifulSoup(page.html_content, "html.parser")
            
            headline = soup.find("h1.Page-headline")
            headline_text = headline.text.strip() if headline else ""
            
            content_div = soup.find("main", {"class": "Page-main"})
            if not content_div:
                raise Exception("Malformed HTML: main content not found")
                
            paragraphs = content_div.find_all("p")
            content = " ".join([p.text.strip() for p in paragraphs])
            
            return Article(url=url, headline=headline_text, content=content)
            
        except Exception as e:
            print(f"Error processing article {url}: {str(e)}")
            return None
