from typing import Dict, Any, List
from product_data import RAW_PRODUCT_DATA
from models import Product, Question, Page
from templates import TemplateEngine
from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent
from agents.file_writer_agent import FileWriterAgent


class Orchestrator:
    def __init__(self, raw_product_data: Dict[str, Any]) -> None:
        self.raw_product_data = raw_product_data
        self.template_engine = TemplateEngine()

        self.parser_agent = ProductParserAgent()
        self.question_agent = QuestionGenerationAgent()
        self.faq_page_agent = FAQPageAgent(self.template_engine)
        self.product_page_agent = ProductPageAgent(self.template_engine)
        self.comparison_page_agent = ComparisonPageAgent(self.template_engine)
        self.file_writer_agent = FileWriterAgent()

    def run(self) -> Dict[str, str]:
        """
        Run the full pipeline and return the paths of the generated JSON files.
        """
        # 1. Parse raw data -> Product
        product: Product = self.parser_agent.run(self.raw_product_data)

        # 2. Generate questions
        questions: List[Question] = self.question_agent.run(product)

        # 3. Generate pages
        faq_page: Page = self.faq_page_agent.run((product, questions))
        product_page: Page = self.product_page_agent.run(product)
        comparison_page: Page = self.comparison_page_agent.run(product)

        # 4. Write pages to disk
        faq_path = self.file_writer_agent.run((faq_page, "output/faq.json"))
        product_page_path = self.file_writer_agent.run(
            (product_page, "output/product_page.json")
        )
        comparison_page_path = self.file_writer_agent.run(
            (comparison_page, "output/comparison_page.json")
        )

        # 👉 THIS RETURN IS CRUCIAL
        return {
            "faq": faq_path,
            "product_page": product_page_path,
            "comparison_page": comparison_page_path,
        }
