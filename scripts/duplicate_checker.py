import os
import glob
from difflib import SequenceMatcher
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_duplicate(new_question: str, questions_dir: str = "../questions", threshold: float = 0.8) -> bool:
    """
    Checks if the newly generated question is too similar to any existing question.
    Returns True if similarity > threshold, else False.
    """
    if not os.path.exists(questions_dir):
        logging.warning(f"Questions directory {questions_dir} does not exist. Skipping duplicate check.")
        return False
        
    existing_files = glob.glob(os.path.join(questions_dir, "*.md"))
    existing_questions = []
    
    for file_path in existing_files:
        with open(file_path, "r", encoding="utf-8") as f:
            existing_questions.append(f.read())
            
    if not existing_questions:
        logging.info("No existing questions found. New question is unique.")
        return False
        
    try:
        max_similarity = 0.0
        for eq in existing_questions:
            # Calculate similarity ratio using SequenceMatcher
            ratio = SequenceMatcher(None, new_question, eq).ratio()
            if ratio > max_similarity:
                max_similarity = ratio
        
        logging.info(f"Max similarity found: {max_similarity:.2f}")
        
        if max_similarity > threshold:
            logging.warning(f"Duplicate found! Similarity {max_similarity:.2f} exceeds threshold {threshold}.")
            return True
            
        return False
        
    except Exception as e:
        logging.error(f"Error during duplicate detection: {e}")
        return False
