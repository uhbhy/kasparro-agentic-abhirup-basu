# agents/question_agent.py

from typing import List
from agents.base import Agent
from models import Product, Question
from content_blocks import generate_questions


class QuestionGenerationAgent(Agent):
    """
    Responsibility: generate categorized user questions from Product.
    """

    def run(self, product: Product) -> List[Question]:
        questions = generate_questions(product)
        # Enforce minimum
        if len(questions) < 15:
            raise ValueError("Expected at least 15 questions.")
        return questions
