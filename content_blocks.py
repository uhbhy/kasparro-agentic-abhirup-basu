# content_blocks.py

from typing import List, Dict, Any
from models import Product, Question, QuestionCategory, FAQItem, ComparisonProduct


# ---------- Utility / core blocks ----------

def generate_product_summary_block(product: Product) -> str:
    """Short summary using only available facts."""
    skin_types = ", ".join(product.skin_types)
    benefits = ", ".join(product.benefits)
    ingredients = ", ".join(product.key_ingredients)

    return (
        f"{product.name} is a {product.concentration} serum designed for {skin_types} skin. "
        f"It contains {ingredients} and helps with {benefits.lower()}."
    )


def generate_usage_block(product: Product) -> str:
    return product.how_to_use


def generate_safety_block(product: Product) -> str:
    return (
        f"Side effects: {product.side_effects} If irritation persists, consider reducing frequency or discontinuing use."
    )


def generate_ingredients_block(product: Product) -> Dict[str, Any]:
    return {
        "key_ingredients": product.key_ingredients,
        "concentration": product.concentration,
    }


def generate_benefits_block(product: Product) -> List[str]:
    return product.benefits


def generate_pricing_block(product: Product) -> Dict[str, Any]:
    return {
        "price": product.price,
        "currency": "INR",
        "display_price": product.price,
    }


# ---------- Question generation logic ----------

def _make_question(text: str, category: QuestionCategory) -> Question:
    return Question(text=text, category=category)


def generate_questions(product: Product) -> List[Question]:
    """
    Generate at least 15 categorized user questions, based only on available info.
    """
    questions: List[Question] = []

    # Informational
    questions.append(_make_question(
        f"What does {product.name} do?", "informational"
    ))
    questions.append(_make_question(
        f"What are the key ingredients in {product.name}?", "informational"
    ))
    questions.append(_make_question(
        f"Which skin types is {product.name} suitable for?", "informational"
    ))
    questions.append(_make_question(
        f"What is the Vitamin C concentration in {product.name}?", "informational"
    ))

    # Usage
    questions.append(_make_question(
        f"How should I use {product.name} in my routine?", "usage"
    ))
    questions.append(_make_question(
        f"Can I use {product.name} in the morning?", "usage"
    ))
    questions.append(_make_question(
        f"How many drops of {product.name} should I apply?", "usage"
    ))
    questions.append(_make_question(
        f"Do I need to use sunscreen after applying {product.name}?", "usage"
    ))

    # Safety
    questions.append(_make_question(
        f"Are there any side effects of using {product.name}?", "safety"
    ))
    questions.append(_make_question(
        f"Is {product.name} suitable for sensitive skin?", "safety"
    ))
    questions.append(_make_question(
        f"What should I do if I feel tingling after applying {product.name}?", "safety"
    ))

    # Purchase
    questions.append(_make_question(
        f"What is the price of {product.name}?", "purchase"
    ))
    questions.append(_make_question(
        f"Is {product.name} affordable for daily use?", "purchase"
    ))

    # Comparison (high level, generic)
    questions.append(_make_question(
        f"How does {product.name} compare to other Vitamin C serums?", "comparison"
    ))
    questions.append(_make_question(
        f"Does {product.name} offer the same benefits as other brightening serums?", "comparison"
    ))

    return questions


# ---------- FAQ generation logic ----------

def generate_faq_items(product: Product, questions: List[Question]) -> List[FAQItem]:
    """
    Turn selected questions into Q&A pairs using only known product info.
    We'll pick a subset but you can extend to all 15+.
    """

    # Map simple answers from available info
    answer_map = {
        "What does": generate_product_summary_block(product),
        "What are the key ingredients": (
            f"The key ingredients are {', '.join(product.key_ingredients)}."
        ),
        "Which skin types": (
            f"It is suitable for {', '.join(product.skin_types)} skin."
        ),
        "What is the Vitamin C concentration": (
            f"It contains {product.concentration}."
        ),
        "How should I use": product.how_to_use,
        "How many drops": "Use 2–3 drops per application, as suggested.",
        "Do I need to use sunscreen": (
            "Yes, it is suggested to use it in the morning before sunscreen, "
            "so you should apply sunscreen after using the serum."
        ),
        "Are there any side effects": product.side_effects,
        "Is": f"{product.name} may cause mild tingling for sensitive skin.",
        "What should I do if I feel tingling": (
            "Mild tingling can occur on sensitive skin. If the sensation is strong or persists, "
            "consider reducing usage frequency or stopping use."
        ),
        "What is the price": f"The price is {product.price}.",
    }

    faq_items: List[FAQItem] = []

    for q in questions:
        answer = None
        # Simple prefix-based matching to keep it deterministic
        for prefix, a in answer_map.items():
            if q.text.startswith(prefix):
                answer = a
                break

        # For unmatched questions, we still generate safe, data-grounded text
        if answer is None:
            if q.category == "comparison":
                answer = (
                    f"{product.name} is a {product.concentration} serum with "
                    f"{', '.join(product.key_ingredients)} that focuses on "
                    f"{', '.join(product.benefits).lower()}. Specific comparisons depend on the other product."
                )
            elif q.category == "purchase":
                answer = f"{product.name} is priced at {product.price}."

        if answer is not None:
            faq_items.append(FAQItem(question=q.text, answer=answer, category=q.category))

    return faq_items


# ---------- Comparison blocks ----------

def generate_fictional_comparison_product() -> ComparisonProduct:
    """
    Create a fictional Product B with structured fields.
    This is intentionally not based on any external data.
    """
    return ComparisonProduct(
        name="ClearRadiance Brightening Serum",
        key_ingredients=["Vitamin C", "Niacinamide"],
        benefits=["Brightening", "Helps with uneven tone"],
        price="₹849",
    )


def compare_ingredients_block(a: Product, b: ComparisonProduct) -> Dict[str, Any]:
    a_set = set(a.key_ingredients)
    b_set = set(b.key_ingredients)
    return {
        "common_ingredients": sorted(list(a_set & b_set)),
        "only_in_glowboost": sorted(list(a_set - b_set)),
        "only_in_product_b": sorted(list(b_set - a_set)),
    }


def compare_benefits_block(a: Product, b: ComparisonProduct) -> Dict[str, Any]:
    a_set = set(a.benefits)
    b_set = set(b.benefits)
    return {
        "common_benefits": sorted(list(a_set & b_set)),
        "only_glowboost_benefits": sorted(list(a_set - b_set)),
        "only_product_b_benefits": sorted(list(b_set - a_set)),
    }


def compare_pricing_block(a: Product, b: ComparisonProduct) -> Dict[str, Any]:
    def extract_numeric(price_str: str) -> float:
        digits = "".join(ch for ch in price_str if ch.isdigit())
        return float(digits) if digits else 0.0

    a_price = extract_numeric(a.price)
    b_price = extract_numeric(b.price)

    if a_price < b_price:
        relation = "glowboost_cheaper"
    elif a_price > b_price:
        relation = "glowboost_more_expensive"
    else:
        relation = "same_price"

    return {
        "glowboost_price": a.price,
        "product_b_price": b.price,
        "price_relation": relation,
    }
