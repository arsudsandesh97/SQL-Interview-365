# 🚀 SQL-Interview-365

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

**Total Questions Generated**: 24
**Last Updated**: July 09, 2026

### 🆕 Most Recent Questions

- 📝 [Day 024 - SQL Challenge](questions/day-024.md)
- 📝 [Day 023 - SQL Challenge](questions/day-023.md)
- 📝 [Day 022 - SQL Challenge](questions/day-022.md)
- 📝 [Day 021 - SQL Challenge](questions/day-021.md)
- 📝 [Day 020 - SQL Challenge](questions/day-020.md)
- 📝 [Day 019 - SQL Challenge](questions/day-019.md)
- 📝 [Day 018 - SQL Challenge](questions/day-018.md)
- 📝 [Day 017 - SQL Challenge](questions/day-017.md)
- 📝 [Day 016 - SQL Challenge](questions/day-016.md)
- 📝 [Day 015 - SQL Challenge](questions/day-015.md)

---

## 👤 Author

**Sandesh Arsud**
- **GitHub**: [@arsudsandesh97](https://github.com/arsudsandesh97)

---

*Generated automatically with ❤️ by SQL-Interview-365 Bot.*
