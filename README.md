# 📊 IndiaMART Industrial Machinery Data Pipeline

## 🔹 Overview
This project demonstrates an end-to-end data engineering workflow, including web scraping, data cleaning, exploratory data analysis (EDA), and visualization.
---
## 🔧 Tech Stack
- Python3 (VS Code)
- Playwright (Web Scraping)  
- Pandas (Data Processing)  
- Matplotlib & Seaborn (Visualization)  
- Jupyter Notebook (EDA)  

---

## ⚙️ Workflow
1. Created virtual environment inside VS code
2. Scraped product data from IndiaMART using Playwright  
3. Stored raw data in JSON format  
4. Cleaned and transformed data using Pandas  
5. Performed EDA and created visualizations  
6. Generated insights and hypotheses  
---
## 📊 Key Insights
- Most products fall in mid-to-high price range  
- Industrial hubs like Mumbai and Surat dominate supplier distribution  
- Weak correlation between price and rating  
- Strong focus on automation-based machinery  
---
## 🧠 Hypothesis
Higher-rated suppliers are more likely to be trusted and preferred in the market.
---
## 📌 Conclusion
- This project highlights how raw web data can be transformed into actionable insights using a structured data pipeline.
---
## ▶️ How to Run
```bash
pip install -r requirements.txt
python scraper/scraper.py

