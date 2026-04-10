# 🏢 AI Company Brochure Generator

An AI-powered tool that automatically scrapes a company's website, identifies relevant pages, and generates a polished marketing brochure using OpenAI's GPT models.

## Overview

This project takes a company name and its website URL as input, then:

1. **Scrapes** the landing page content and extracts all links.
2. **Selects** the most relevant links (About, Careers, Company pages, etc.) using `gpt-5-nano`.
3. **Fetches** the content from those relevant pages.
4. **Generates** a comprehensive brochure in Markdown format using `gpt-4.1-mini`.

The resulting brochure includes information about the company's mission, culture, customers, and career opportunities — useful for prospective customers, investors, and recruits.

## Installation

1. **Clone the repository:**

   ```bash
    git clone https://github.com/onyevyerov/brochure-generator.git
    cd brochure-generator

2. **Create and activate a virtual environment (recommended):**

   ```bash
    python -m venv venv
    source venv/bin/activate        # macOS / Linux
    venv\Scripts\activate           # Windows

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Create a .env file in the project root:**

   ```bash
   OPENAI_API_KEY=sk-your-api-key-here

5. **Run main.py file**