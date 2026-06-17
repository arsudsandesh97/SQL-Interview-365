import os
import glob
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_readme(questions_dir: str = "questions", readme_path: str = "README.md"):
    """
    Updates the README.md with the latest question stats and a beautiful layout.
    """
    # Fix paths if running from scripts/ directory
    if not os.path.exists(questions_dir) and os.path.exists(f"../{questions_dir}"):
        questions_dir = f"../{questions_dir}"
        readme_path = f"../{readme_path}"

    existing_files = glob.glob(os.path.join(questions_dir, "day-*.md"))
    
    day_numbers = []
    for file_path in existing_files:
        basename = os.path.basename(file_path) # e.g. day-001.md
        try:
            day_num = int(basename.replace("day-", "").replace(".md", ""))
            day_numbers.append(day_num)
        except ValueError:
            pass
            
    day_numbers.sort(reverse=True)
    total_questions = len(day_numbers)
    
    if total_questions == 0:
        recent_list = "*No questions generated yet.*"
    else:
        recent_list_links = []
        for num in day_numbers[:10]: # show up to top 10
            recent_list_links.append(f"- 📝 [Day {num:03d} - SQL Challenge](questions/day-{num:03d}.md)")
        recent_list = "\n".join(recent_list_links)
        
    current_date = datetime.now().strftime("%B %d, %Y")
    
    readme_content = f"""# 🚀 SQL-Interview-365

![GitHub Action](https://img.shields.io/badge/GitHub%20Action-Active-success)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Gemini API](https://img.shields.io/badge/Gemini%20API-Powered-orange)
![SQL](https://img.shields.io/badge/SQL-Interview%20Prep-lightgrey)

A fully automated, zero-maintenance project that generates **one unique, scenario-based SQL interview question every single day**! 

Designed specifically for Data Analysts, Data Engineers, and BI Professionals to sharpen their SQL skills consistently.

---

## 🎯 How It Works

This repository is powered by a **GitHub Actions** cron job that runs daily at `02:30 UTC` (08:00 AM IST). 

1. **AI Generation**: A Python script calls the **Google Gemini 2.5 Flash API** to generate a highly realistic, scenario-based SQL question.
2. **Duplicate Check**: The script ensures the question is unique (comparing similarity to past questions).
3. **Storage**: The generated question is saved as a Markdown file in the `questions/` directory.
4. **Notification**: The system automatically emails the new question directly to the repository owner.
5. **Dashboard Update**: This `README.md` is automatically updated to reflect the latest questions!

---

## 📁 Repository Structure

```text
📦 SQL-Interview-365
 ┣ 📂 questions/          # All daily generated SQL questions
 ┣ 📂 scripts/            # Automation logic
 ┃ ┣ 📜 main.py           # Orchestrator
 ┃ ┣ 📜 generate_question.py
 ┃ ┣ 📜 duplicate_checker.py
 ┃ ┣ 📜 save_question.py
 ┃ ┣ 📜 send_email.py
 ┃ ┗ 📜 update_readme.py  # Self-updates this README
 ┣ 📜 .env.example        # Environment variables template
 ┣ 📜 requirements.txt    # Python dependencies
 ┗ 📜 README.md           # You are here!
```

---

## 📊 Daily Dashboard

**Total Questions Generated**: {total_questions}
**Last Updated**: {current_date}

### 🆕 Most Recent Questions

{recent_list}

---

*Generated automatically with ❤️ by SQL-Interview-365 Bot.*
"""
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    logging.info("README.md updated successfully with new formatting.")

