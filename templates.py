# templates.py

from typing import Dict, Any, List
from models import Product, FAQItem, Page
from models import ComparisonProduct
import content_blocks as blocks


class TemplateEngine:
    """
    Simple template engine that orchestrates content blocks based on template type.
    """

    def render_faq_page(self, product: Product, faq_items: List[FAQItem]) -> Page:
        # At least 5 Q&A enforced here (or earlier in orchestration).
        faq_payload: Dict[str, Any] = {
            "title": f"{product.name} – Frequently Asked Questions",
            "product_name": product.name,
            "faqs": [
                {
                    "question": item.question,
                    "answer": item.answer,
                    "category": item.category,
                }
                for item in faq_items
            ],
        }
        return Page(page_type="faq", payload=faq_payload)

    def render_product_page(self, product: Product) -> Page:
        summary = blocks.generate_product_summary_block(product)
        usage = blocks.generate_usage_block(product)
        safety = blocks.generate_safety_block(product)
        ingredients_block = blocks.generate_ingredients_block(product)
        benefits_block = blocks.generate_benefits_block(product)
        price_block = blocks.generate_pricing_block(product)

        payload: Dict[str, Any] = {
            "title": product.name,
            "product_name": product.name,
            "summary": summary,
            "sections": {
                "ingredients": ingredients_block,
                "benefits": benefits_block,
                "usage": {"how_to_use": usage},
                "safety": {"notes": safety},
                "pricing": price_block,
            },
        }
        return Page(page_type="product_page", payload=payload)

    def render_comparison_page(
        self, glowboost: Product, product_b: ComparisonProduct
    ) -> Page:
        ingredients_comp = blocks.compare_ingredients_block(glowboost, product_b)
        benefits_comp = blocks.compare_benefits_block(glowboost, product_b)
        pricing_comp = blocks.compare_pricing_block(glowboost, product_b)

        payload: Dict[str, Any] = {
            "title": f"{glowboost.name} vs {product_b.name}",
            "products": {
                "glowboost": {
                    "name": glowboost.name,
                    "key_ingredients": glowboost.key_ingredients,
                    "benefits": glowboost.benefits,
                    "price": glowboost.price,
                },
                "product_b": {
                    "name": product_b.name,
                    "key_ingredients": product_b.key_ingredients,
                    "benefits": product_b.benefits,
                    "price": product_b.price,
                },
            },
            "comparison": {
                "ingredients": ingredients_comp,
                "benefits": benefits_comp,
                "pricing": pricing_comp,
            },
        }
        return Page(page_type="comparison_page", payload=payload)
