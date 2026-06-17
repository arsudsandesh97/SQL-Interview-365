import os
import glob
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_question(question_text: str, questions_dir: str = "../questions") -> int:
    """
    Saves the question text to a new file in the questions_dir.
    Returns the day number.
    """
    if not os.path.exists(questions_dir):
        os.makedirs(questions_dir)
        
    existing_files = glob.glob(os.path.join(questions_dir, "day-*.md"))
    
    max_day = 0
    for file_path in existing_files:
        basename = os.path.basename(file_path) # e.g. day-001.md
        try:
            day_num = int(basename.replace("day-", "").replace(".md", ""))
            if day_num > max_day:
                max_day = day_num
        except ValueError:
            pass
            
    next_day = max_day + 1
    
    file_name = f"day-{next_day:03d}.md"
    file_path = os.path.join(questions_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(question_text)
        
    logging.info(f"Question saved to {file_path}")
    return next_day
