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

**Total Questions Generated**: 68
**Last Updated**: August 22, 2026

### 🆕 Most Recent Questions

- 📝 [Day 068 - SQL Challenge](questions/day-068.md)
- 📝 [Day 067 - SQL Challenge](questions/day-067.md)
- 📝 [Day 066 - SQL Challenge](questions/day-066.md)
- 📝 [Day 065 - SQL Challenge](questions/day-065.md)
- 📝 [Day 064 - SQL Challenge](questions/day-064.md)
- 📝 [Day 063 - SQL Challenge](questions/day-063.md)
- 📝 [Day 062 - SQL Challenge](questions/day-062.md)
- 📝 [Day 061 - SQL Challenge](questions/day-061.md)
- 📝 [Day 060 - SQL Challenge](questions/day-060.md)
- 📝 [Day 059 - SQL Challenge](questions/day-059.md)

---

## 👤 Author

**Sandesh Arsud**
- **GitHub**: [@arsudsandesh97](https://github.com/arsudsandesh97)

---

*Generated automatically with ❤️ by SQL-Interview-365 Bot.*
