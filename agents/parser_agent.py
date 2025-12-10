# agents/parser_agent.py

from typing import Dict, Any
from agents.base import Agent
from models import Product


class ProductParserAgent(Agent):
    """
    Responsibility: parse raw dict-like data into a Product model.
    """

    def run(self, input_data: Dict[str, Any]) -> Product:
        return Product(
            name=input_data["product_name"],
            concentration=input_data["concentration"],
            skin_types=list(input_data["skin_type"]),
            key_ingredients=list(input_data["key_ingredients"]),
            benefits=list(input_data["benefits"]),
            how_to_use=input_data["how_to_use"],
            side_effects=input_data["side_effects"],
            price=input_data["price"],
        )
