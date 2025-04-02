"""
Main entry point for the scraping system.
"""
import argparse
from typing import List, Optional

from .models import Article
from .scrapers import APNewsScraper
from .storage import FileStorage, KafkaStorage


def scrape_ap_news(max_articles: int = 10) -> List[Article]:
    """
    Scrape articles from AP News.

    Args:
        max_articles: Maximum number of articles to scrape

    Returns:
        List of Article objects
    """
    scraper = APNewsScraper()
    return scraper.get_articles(max_articles=max_articles)


def save_articles(articles: List[Article],
                  format: str = "file", **kwargs) -> Optional[str]:
    """
    Save articles to the specified storage.

    Args:
        articles: List of Article objects to save
        format: Storage format, one of "file" or "kafka"
        **kwargs: Additional arguments for the storage class

    Returns:
        Filename if saved to file, None otherwise
    """
    if format.lower() == "file":
        return FileStorage.save_articles(articles, **kwargs)
    elif format.lower() == "kafka":
        KafkaStorage.save_articles(articles, **kwargs)
        return None
    else:
        raise ValueError(f"Unsupported storage format: {format}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Scrape news articles")
    parser.add_argument("--max-articles", type=int, default=10,
                        help="Maximum number of articles to scrape")
    parser.add_argument(
        "--format", choices=["file", "kafka"], default="file", help="Storage format")
    parser.add_argument("--filename", help="Filename for file storage")
    parser.add_argument("--kafka-topic", default="articles",
                        help="Kafka topic for kafka storage")
    parser.add_argument(
        "--kafka-servers", default="localhost:9092", help="Kafka bootstrap servers")

    args = parser.parse_args()

    # Scrape articles
    articles = scrape_ap_news(max_articles=args.max_articles)

    # Save articles
    if args.format == "file":
        filename = save_articles(
            articles, format="file", filename=args.filename)
        print(f"Saved {len(articles)} articles to {filename}")
    else:
        save_articles(
            articles,
            format="kafka",
            topic=args.kafka_topic,
            servers=args.kafka_servers
        )
        print(
            f"Saved {len(articles)} articles to Kafka topic {args.kafka_topic}")


if __name__ == "__main__":
    main()
