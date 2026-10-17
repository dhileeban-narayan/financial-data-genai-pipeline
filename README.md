\# Financial Market Data Pipeline \& GenAI Governance



An end-to-end, automated data engineering pipeline that extracts daily equity market data, transforms it for business intelligence consumption, and utilizes Google's Gemini LLM for programmatic data quality governance.



This project demonstrates the transition from traditional, manual ETL workflows to modern, AI-assisted cloud engineering, focusing on high reliability and strict data validation.



\## 🏗️ Architecture \& Tech Stack

\* \*\*Data Integration:\*\* Python (Pandas, Requests)

\* \*\*Data Storage \& Modeling:\*\* PostgreSQL (Star Schema for downstream Power BI consumption)

\* \*\*AI \& Governance:\*\* Google GenAI SDK (Gemini 2.5 Flash), Pydantic

\* \*\*Workflow:\*\* Extract (API) ➔ Transform (Python) ➔ Load (SQL Upserts) ➔ Validate (GenAI Agent)



\## 🚀 Key Features



1\. \*\*Automated ETL Pipeline:\*\* Ingests live financial tick data, handles missing values, calculates moving averages, and executes idempotent `MERGE` operations into the database to prevent data duplication.

2\. \*\*GenAI Data Quality Agent:\*\* Integrates the Gemini API to act as a programmatic governance watchdog. It analyzes daily load metadata (row counts, null percentages, extreme standard deviations).

3\. \*\*Structured LLM Output:\*\* Utilizes Pydantic to force the GenAI model to return strict, machine-readable JSON objects (Status, Anomalies, Recommended Actions) allowing the pipeline to automatically halt on critical failures.

4\. \*\*Enterprise Dimensional Modeling:\*\* Data is structured into Fact and Dimension tables, abstracting backend complexity and delivering clean, validated datasets ready for BI teams.



\## 📂 Repository Structure

```text

financial-data-genai-pipeline/

├── docs/

│   └── ERD\_schema.png        # Visual data model (Fact/Dim tables)

├── sql/

│   ├── 01\_ddl\_tables.sql     # PostgreSQL table creation scripts

│   └── 02\_views.sql          # Downstream views for Power BI

├── src/

│   ├── extract\_api.py        # Python script to pull market data 

│   ├── transform\_clean.py    # Python/Pandas logic for cleansing

│   └── load\_db.py            # Logic to upsert data into the warehouse

└── genai\_agent/

&#x20;   └── dq\_monitor\_agent.py   # Gemini Enterprise agent for data quality

