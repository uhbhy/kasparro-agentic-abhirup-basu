# models.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Any


QuestionCategory = Literal["informational", "usage", "safety", "purchase", "comparison"]


@dataclass
class Product:
    name: str
    concentration: str
    skin_types: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str


@dataclass
class Question:
    text: str
    category: QuestionCategory


@dataclass
class FAQItem:
    question: str
    answer: str
    category: QuestionCategory


@dataclass
class Page:
    """Base class for all pages."""
    page_type: str
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ComparisonProduct:
    name: str
    key_ingredients: List[str]
    benefits: List[str]
    price: str
