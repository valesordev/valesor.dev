"""
Storage mechanisms for saving scraped articles.
"""
import json
import os
from datetime import datetime
from typing import List, Optional

from .models import Article


class BaseStorage:
    """Base class for all storage mechanisms."""

    @classmethod
    def save_articles(cls, articles: List[Article], **kwargs):
        """Save articles to storage."""
        pass


class FileStorage(BaseStorage):
    """Storage implementation that saves articles to a JSON file."""

    @classmethod
    def save_articles(cls, articles: List[Article], filename: Optional[str] = None, directory: str = "") -> str:
        """
        Saves articles to a JSON file with timestamp.

        Args:
            articles: List of Article objects to save
            filename: Optional filename, will generate one based on timestamp if not provided
            directory: Optional directory to save the file in

        Returns:
            The filename of the saved file
        """
        if filename is None:
            filename = f"articles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        if directory:
            os.makedirs(directory, exist_ok=True)
            filepath = os.path.join(directory, filename)
        else:
            filepath = filename

        # Convert articles to dictionary representations
        articles_data = [article.to_dict() for article in articles]

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(articles_data, f, ensure_ascii=False, indent=2)

        return filepath


class KafkaStorage(BaseStorage):
    """Storage implementation that saves articles to a Kafka topic."""

    @classmethod
    def save_articles(cls, articles: List[Article], topic: str = "articles", servers: str = "localhost:9092"):
        """
        Save articles to a Kafka topic as JSON messages.

        Args:
            articles: List of Article objects to save
            topic: Kafka topic to publish to
            servers: Comma-separated list of Kafka bootstrap servers
        """
        try:
            from kafka import KafkaProducer

            producer = KafkaProducer(
                bootstrap_servers=servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )

            for article in articles:
                producer.send(topic, article.to_dict())

            producer.flush()
            return True
        except Exception as e:
            print(f"Error saving to Kafka: {str(e)}")
            return False
