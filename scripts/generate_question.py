import os
import google.generativeai as genai
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_sql_question() -> str:
    """
    Generates a unique SQL scenario-based interview question using Gemini API.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    genai.configure(api_key=api_key)
    
    # We will use gemini-2.5-flash as the default model
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = """Generate one unique SQL scenario-based interview question.

Requirements:
- Medium to Hard difficulty
- Real business use case
- Suitable for Data Analyst interviews
- Avoid common LeetCode SQL50 problems
- Avoid repeating previously generated questions
- Focus on domains such as Retail, E-commerce, Finance, Healthcare, Logistics, Marketing, Operations, HR, SaaS, Manufacturing

You MUST format the output EXACTLY like this template:

# SQL Scenario-Based Interview Question: [Question Title]

## Business Scenario
[Provide a realistic business scenario, role, and problem]

Assume:
```sql
CURRENT_DATE = '[YYYY-MM-DD]'
```

---

# Database Setup

## Create [Table1] Table
```sql
[CREATE TABLE statement]
```

## Insert [Table1] Data
```sql
[INSERT INTO statement]
```
*(Repeat Create and Insert for all necessary tables)*

---

# Input Tables

### [Table1]
[Markdown table of data]
*(Repeat for all necessary tables)*

---

# Task
[Clearly state the problem and any conditions to apply]

---

# Expected Output Format
[Markdown table showing expected output]

---

# Skills Tested
* [Skill 1]
* [Skill 2]

Return ONLY the raw markdown matching this exact structure."""
    
    logging.info("Calling Gemini API to generate a question...")
    response = model.generate_content(prompt)
    
    if not response.text:
        raise RuntimeError("Failed to generate content from Gemini API")
        
    return response.text

if __name__ == "__main__":
    # Test generation if run directly
    print(generate_sql_question())
