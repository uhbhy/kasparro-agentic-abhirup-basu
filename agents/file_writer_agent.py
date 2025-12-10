# agents/file_writer_agent.py

import json
from pathlib import Path
from typing import Tuple
from agents.base import Agent
from models import Page


class FileWriterAgent(Agent):
    """
    Responsibility: write Page objects to JSON files.
    Input: (Page, output_path)
    Output: output_path (string)
    """

    def run(self, input_data: Tuple[Page, str]) -> str:
        page, output_path = input_data
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "page_type": page.page_type,
            "payload": page.payload,
        }

        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return str(path)
