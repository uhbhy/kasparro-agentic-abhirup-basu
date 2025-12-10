🌟 Agentic Content Generation System

A modular multi-agent automation pipeline that transforms a small structured product dataset into complete, machine-readable JSON content pages.

The system simulates real-world deterministic agentic workflows used in enterprise AI content engines.

🚀 What This System Produces

From a minimal product dataset, the pipeline generates:

faq.json — Categorized FAQ page

product_page.json — Product description page

comparison_page.json — Comparison page vs. a fictional competitor

questions.json (optional) — All generated user questions

All content is produced purely from the provided dataset using rule-based logic —
no external knowledge, scraping, or APIs.

🎯 System Goals

Build a modular, deterministic multi-agent system

Demonstrate automation graphs, reusable content logic layers, and template assembly

Generate clean, stable JSON outputs

Show strong engineering design & abstraction

🏗️ Architecture Overview

The system follows a deterministic multi-agent flow, where each agent has a single responsibility and communicates through strict JSON-structured inputs/outputs.

📦 High-Level Pipeline
flowchart TD
    A[RAW_PRODUCT_DATA] --> B[ProductParserAgent]

    B -->|Product| C[QuestionGenerationAgent]

    C -->|Questions| D[FAQPageAgent]
    C -->|Questions| H[QuestionListPageAgent]

    B --> E[ProductPageAgent]
    B --> F[ComparisonPageAgent]

    D -->|FAQ Page| G1[FileWriterAgent]
    E -->|Product Page| G2[FileWriterAgent]
    F -->|Comparison Page| G3[FileWriterAgent]
    H -->|Questions Page| G4[FileWriterAgent]

    G1 --> I[faq.json]
    G2 --> J[product_page.json]
    G3 --> K[comparison_page.json]
    G4 --> L[questions.json]

🧩 System Components
🟦 1. Models (models.py)

Defines all internal structured data types:

Product

Question, FAQItem

ComparisonProduct

Page (generic page container)

These enforce strict, predictable schemas.

🟦 2. Content Logic Blocks (content_blocks.py)

Pure deterministic functions used to generate content.

Examples (Product Content):

generate_product_summary_block

generate_usage_block

generate_safety_block

generate_benefits_block

generate_pricing_block

Question Generation:

generate_questions (15+ categorized types)

Comparison Logic:

compare_ingredients_block

compare_benefits_block

compare_pricing_block

These blocks ensure repeatable, rule-driven content generation.

🟦 3. Template Engine (templates.py)

A lightweight custom template assembler that constructs full Page JSON objects.

Templates Implemented:

FAQ Page Template

Product Page Template

Comparison Page Template

Outputs are strictly machine-readable, not natural language documents.

🟦 4. Multi-Agent Layer (agents/)

Each agent performs exactly one responsibility:

Agent	Responsibility
ProductParserAgent	Convert raw dict → Product model
QuestionGenerationAgent	Create categorized questions
FAQPageAgent	Build FAQ page
ProductPageAgent	Build product detail page
ComparisonPageAgent	Build comparison page
QuestionListPageAgent	Export all generated questions
FileWriterAgent	Save Page objects to .json

All agents follow strict input → output contracts.

🟦 5. Orchestrator (orchestration.py)

Coordinates the complete system:

Constructs all agents

Defines the DAG (automation graph)

Routes outputs between agents

Saves final JSON files into /output

Ensures a run is fully deterministic.

📂 Folder Structure
Kasparo/
│
├── agents/
│   ├── base.py
│   ├── parser_agent.py
│   ├── question_agent.py
│   ├── faq_page_agent.py
│   ├── product_page_agent.py
│   ├── comparison_page_agent.py
│   ├── question_export_agent.py
│   └── file_writer_agent.py
│
├── content_blocks.py
├── templates.py
├── models.py
├── product_data.py
├── orchestration.py
├── main.py
│
└── output/
    ├── faq.json
    ├── product_page.json
    ├── comparison_page.json
    └── questions.json

🧭 Design Principles
✔ Single Responsibility Agents

One task per agent → scalable, maintainable, clean.

✔ Deterministic Logic

No randomness, LLM calls, or external data.

✔ Modular & Extensible

Adding a new page or agent requires minimal code.

✔ Strict Machine-Readable Output

All outputs follow defined JSON schemas.

✔ Inspired by Real Industry Pipelines

Simulates real-world AI content automation systems.
