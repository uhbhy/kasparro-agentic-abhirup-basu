# agents/faq_page_agent.py

from typing import List, Tuple
from agents.base import Agent
from models import Product, Question, FAQItem, Page
from content_blocks import generate_faq_items
from templates import TemplateEngine


class FAQPageAgent(Agent):
    """
    Responsibility: generate FAQ items and render FAQ page JSON.
    Input: (Product, List[Question])
    Output: Page (page_type="faq")
    """

    def __init__(self, template_engine: TemplateEngine) -> None:
        self.template_engine = template_engine

    def run(self, input_data: Tuple[Product, List[Question]]) -> Page:
        product, questions = input_data
        faq_items: List[FAQItem] = generate_faq_items(product, questions)

        # Enforce at least 5 Q&A
        if len(faq_items) < 5:
            raise ValueError("FAQ requires at least 5 Q&A items.")

        # You could choose top 5 or use all; here we use all.
        page = self.template_engine.render_faq_page(product, faq_items)
        return page
