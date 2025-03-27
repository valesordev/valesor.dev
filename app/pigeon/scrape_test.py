"""
Tests for the scraping system.
"""
import unittest
from unittest.mock import patch, Mock, mock_open
import json

from pigeon.models import Article, Page
from pigeon.scrapers import APNewsScraper
from pigeon.storage import FileStorage


class TestAPNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = APNewsScraper()

        # Load test data
        with open("test_data/https_apnews_com.html", "r", encoding="utf-8") as file:
            self.sample_homepage = file.read()

        with open("test_data/https_apnews_com-article.html", "r", encoding="utf-8") as file:
            self.sample_article = file.read()

        # Expected test data
        self.sample_article_url = "https://apnews.com/article/palestinians-unrwa-israel-netanyahu-hamas-refugees-conflict-jerusalem-13e94715d88b094834bd93c48d018bec"

    @patch('requests.Session.get')
    def test_fetch_page(self, mock_get):
        # Mock response for a page
        mock_response = Mock()
        mock_response.text = self.sample_homepage
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Test fetching page
        page = self.scraper.fetch_page(self.scraper.base_url, delay=False)

        # Assertions
        self.assertIsNotNone(page)
        self.assertEqual(page.url, self.scraper.base_url)
        self.assertEqual(page.html_content, self.sample_homepage)

    @patch('requests.Session.get')
    def test_process_article(self, mock_get):
        # Mock response for an article
        mock_response = Mock()
        mock_response.text = self.sample_article
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Test processing article
        article = self.scraper._process_article(self.sample_article_url)

        # Assertions
        self.assertIsNotNone(article)
        self.assertEqual(article.url, self.sample_article_url)
        self.assertIsInstance(article, Article)

    @patch('requests.Session.get')
    def test_get_articles(self, mock_get):
        # Mock responses for homepage and article
        def mock_get_response(*args, **kwargs):
            mock_response = Mock()
            if args[0] == self.scraper.base_url:
                mock_response.text = self.sample_homepage
            else:
                mock_response.text = self.sample_article
            mock_response.status_code = 200
            return mock_response

        mock_get.side_effect = mock_get_response

        # Create a mocked BeautifulSoup that returns our test links
        with patch('bs4.BeautifulSoup') as mock_soup_class:
            mock_soup = Mock()
            mock_soup_class.return_value = mock_soup

            # Mock the find_all to return a list with one article link
            mock_link = Mock()
            # Fix: Configure mock_link to return self.sample_article_url when accessed with ["href"]
            mock_link.__getitem__ = Mock(return_value=self.sample_article_url)
            mock_soup.find_all.return_value = [mock_link]

            # Mock _process_article to return a test article
            with patch.object(self.scraper, '_process_article') as mock_process:
                test_article = Article(
                    url=self.sample_article_url,
                    headline="Test Headline",
                    content="Test Content"
                )
                mock_process.return_value = test_article

                # Test get_articles
                articles = self.scraper.get_articles(max_articles=1)

                # Assertions
                self.assertEqual(len(articles), 1)
                self.assertEqual(articles[0], test_article)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.articles = [
            Article(
                url="https://example.com/article1",
                headline="Test Headline 1",
                content="Test Content 1"
            ),
            Article(
                url="https://example.com/article2",
                headline="Test Headline 2",
                content="Test Content 2"
            )
        ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_articles(self, mock_json_dump, mock_file_open):
        # Test saving articles to file
        filename = "test_articles.json"

        result = FileStorage.save_articles(self.articles, filename=filename)

        # Assertions
        self.assertEqual(result, filename)
        mock_file_open.assert_called_once_with(filename, "w", encoding="utf-8")
        mock_json_dump.assert_called_once()

        # Check that articles were converted to dict
        args, kwargs = mock_json_dump.call_args
        self.assertEqual(len(args[0]), 2)  # Two articles in the list
        self.assertEqual(args[0][0]["url"], self.articles[0].url)
        self.assertEqual(args[0][1]["url"], self.articles[1].url)


if __name__ == "__main__":
    unittest.main()
