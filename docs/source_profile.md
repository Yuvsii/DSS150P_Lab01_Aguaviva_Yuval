# Data Source Profile Analysis

## Profile Takeaways & Observations
* **Customers Data:** The CSV has 250 rows. Running the profiler showed a few missing fields here and there (like missing emails or cities), which we'll need to watch out for during cleaning.
* **Orders & Products:** Both files loaded up cleanly. The JSON orders and Parquet product files have consistent structures without any unexpected corruption or missing keys.
* **API Extraction:** The script successfully hit the REST endpoint and saved a valid JSON snapshot without any connection issues.
* **PostgreSQL Database:** Inspected the `support_tickets` table and verified it contains 250 rows. All the data types (timestamps, integers, text fields) line up properly with what's expected for relational tracking.