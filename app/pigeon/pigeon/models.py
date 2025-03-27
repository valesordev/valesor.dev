"""
Models for the scraping system.
"""
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class Article:
    """Represents a scraped article."""
    url: str
    headline: str
    content: str
    timestamp: str = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert article to dictionary representation."""
        return {
            "url": self.url,
            "headline": self.headline,
            "content": self.content,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }

@dataclass
class Page:
    """Represents a scraped page."""
    url: str
    html_content: str
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
