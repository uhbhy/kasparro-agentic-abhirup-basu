# 🌟 Kasparo Agentic Content Generation System

A modular, multi-agent automation pipeline that transforms a small structured product dataset into fully generated machine-readable JSON content pages.  
This system simulates real-world agentic workflows used in AI-driven content automation engines.

---

# 🚀 Overview

This project ingests a minimal product dataset and autonomously produces:

- **`faq.json`** — A categorized FAQ page  
- **`product_page.json`** — A structured product description page  
- **`comparison_page.json`** — A comparison between the main product and a fictional competitor  
- **(optional)** `questions.json` — All generated user questions  

All content is generated **only from the provided data**, using reusable logic blocks and template rules.  
No external knowledge, scraping, or APIs are used.

---

# 🧠 System Goals

- Build a **modular, agent-based orchestration system**  
- Demonstrate **automation graphs**, **content logic layers**, and **template engines**  
- Produce **clean, deterministic, structured JSON outputs**  
- Show strong engineering design, abstraction, and reasoning  

---

# 🏗️ Architecture Overview

The system follows a **deterministic multi-agent flow**, where each agent has a *single responsibility* and communicates only through structured inputs/outputs.

## 📦 High-Level Pipeline

```mermaid
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
