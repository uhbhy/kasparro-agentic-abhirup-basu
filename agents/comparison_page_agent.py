# agents/comparison_page_agent.py

from agents.base import Agent
from models import Product, Page
from templates import TemplateEngine
from content_blocks import (
    generate_fictional_comparison_product,
)


class ComparisonPageAgent(Agent):
    """
    Responsibility: generate fictional Product B and render comparison page.
    Input: Product (GlowBoost)
    Output: Page (page_type="comparison_page")
    """

    def __init__(self, template_engine: TemplateEngine) -> None:
        self.template_engine = template_engine

    def run(self, glowboost: Product) -> Page:
        product_b = generate_fictional_comparison_product()
        page = self.template_engine.render_comparison_page(glowboost, product_b)
        return page
