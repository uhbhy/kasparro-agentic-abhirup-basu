# agents/product_page_agent.py

from agents.base import Agent
from models import Product, Page
from templates import TemplateEngine


class ProductPageAgent(Agent):
    """
    Responsibility: render standalone product page JSON.
    Input: Product
    Output: Page (page_type="product_page")
    """

    def __init__(self, template_engine: TemplateEngine) -> None:
        self.template_engine = template_engine

    def run(self, product: Product) -> Page:
        return self.template_engine.render_product_page(product)
