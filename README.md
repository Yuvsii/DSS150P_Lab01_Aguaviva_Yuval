# DSS150P Lab 01: Data Profiling & Environment Setup

* **Full Name:** Yuval Ma. Ezekiel B. Aguaviva  
* **Student Number:** 2024100815

## Purpose of the Laboratory
This laboratory focuses on setting up a reproducible local data engineering workspace, profiling multi-format raw datasets, inspecting operational PostgreSQL databases running in Docker, and documenting data flows, schemas, and contracts.

## Software Requirements
* Python 3.14+
* Git
* Docker & Docker Compose
* VS Code

## Exact Steps to Reproduce the Environment
1. Clone the repository and open it in VS Code.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Docker container services:
   ```bash
   docker compose up -d
   ```

## Exact Commands to Start and Stop PostgreSQL
* **Start:** `docker compose up -d`
* **Stop:** `docker compose down`

## How to Run Each Python Script
* **Profile environment:**
  ```bash
  python src/verify_environment.py
  ```
* **Profile raw datasets:**
  ```bash
  python src/profile_sources.py
  ```
* **Inspect REST API snapshot:**
  ```bash
  python src/inspect_api.py
  ```

## Description of Each Source
* **Customers (`data/raw/customers.csv`):** Tabular demographic dataset containing customer IDs, names, emails, and locations.
* **Orders (`data/raw/orders.json`):** Transaction records tracking quantities and fees.
* **Products (`data/raw/products.parquet`):** Columnar inventory file tracking product pricing and categories.
* **API Snapshot (`data/raw/api_snapshot.json`):** Captured REST API payload response data.
* **Support Tickets:** Local operational PostgreSQL container table tracking customer support inquiries.

## Known Limitations or Unresolved Questions
* Optional fields like customer emails and cities occasionally contain missing null values, requiring cleaning logic downstream.

## AI Usage Disclosure
* **Tool Used:** Claude, Google Gemini
* **Assistance Provided:** Helped debug PostgreSQL connection commands, format markdown documentation, and write the lifecycle mapping layout.
* **Verification:** All code, SQL schemas, profile scripts, and written responses were fully reviewed, tested locally in the development environment, and verified by the student prior to final submission.