import os
import glob
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_readme(questions_dir: str = "../questions", readme_path: str = "../README.md"):
    """
    Updates the README.md with the latest question stats.
    """
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
        latest_question = "N/A"
        recent_list = ""
    else:
        latest_question = f"Day {day_numbers[0]}"
        recent_list = "\n".join([f"- Day {num}" for num in day_numbers[:5]])
        
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    readme_content = f"""# SQL Interview 365

Total Questions: {total_questions}

Latest Question:
- {latest_question}

Last Updated:
{current_date}

## Recent Questions

{recent_list}
"""
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    logging.info("README.md updated successfully.")
