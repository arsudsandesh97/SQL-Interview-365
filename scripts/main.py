import sys
import os
import logging
from dotenv import load_dotenv

# Add current directory to path if needed for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_question import generate_sql_question
from duplicate_checker import is_duplicate
from save_question import save_question
from update_readme import update_readme
from send_email import send_question_email

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Load environment variables from .env file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(base_dir, ".env"))
    
    max_retries = 5
    
    # Define paths relative to the script location
    questions_dir = os.path.join(base_dir, "questions")
    readme_path = os.path.join(base_dir, "README.md")
    
    unique_question = None
    
    for attempt in range(1, max_retries + 1):
        logging.info(f"--- Attempt {attempt} of {max_retries} ---")
        try:
            question_text = generate_sql_question()
            
            # Check for duplicates
            if not is_duplicate(question_text, questions_dir=questions_dir, threshold=0.8):
                logging.info("Unique question generated successfully!")
                unique_question = question_text
                break
            else:
                logging.warning("Generated question is too similar to an existing one. Retrying...")
                
        except Exception as e:
            logging.error(f"Error during attempt {attempt}: {e}")
            
    if not unique_question:
        logging.error(f"Failed to generate a unique question after {max_retries} attempts. Exiting.")
        sys.exit(1)
        
    # Save the question
    day_num = save_question(unique_question, questions_dir=questions_dir)
    
    # Update README
    update_readme(questions_dir=questions_dir, readme_path=readme_path)
    
    # Send email notification
    send_question_email(unique_question, day_num)
    
    logging.info("Daily SQL Interview Question process completed successfully.")

if __name__ == "__main__":
    main()
