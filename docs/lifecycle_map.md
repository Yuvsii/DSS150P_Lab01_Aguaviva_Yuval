# Data Engineering Lifecycle Map

## Lifecycle Elements

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | Where data is originally generated or stored. | CSVs, JSON, Parquet files, REST APIs, and PostgreSQL. | Local files / Docker / API endpoint | Upstream system updates, unexpected schema drift, or downtime. |
| **Ingestion/acquisition** | Pulling raw data from sources without changing it. | Python reading files or hitting endpoints via `requests`. | `src/profile_sources.py`, `src/inspect_api.py` | Network time-outs, HTTP errors, or broken paths. |
| **Storage** | Landing raw and structured data for persistence. | Local landing zone (`data/raw/`) and Docker PostgreSQL. | File system / Docker Volumes | Disk space limits, permission bugs, or corrupted volumes. |
| **Processing/transformation** | Cleaning, typing, and structuring raw files for use. | Parsing dates, handling nulls, and building SQL schemas. | Python scripts / SQL schema | Type mismatch bugs or truncation issues. |
| **Data quality/validation** | Checking data against expected business rules. | Validating primary keys, nulls, and value ranges. | Data contracts (`docs/data_contract.yaml`) | Uncaught nulls or bad duplicates sneaking into tables. |
| **Delivery** | Exposing clean tables to downstream users. | Queryable PostgreSQL relational tables ready for use. | PostgreSQL database (`lab.customers`) | Stale data refreshes or broken database links. |
| **Consumer** | End users or applications using the final data. | Fictional analytics team or reporting dashboards. | BI Tools / Analysts | Misinterpreted metrics or wrong business moves. |

## Source Data Flow Diagram

```text
+-------------------+
|  customers.csv    |----+
+-------------------+    |
                         |
+-------------------+    |
|   orders.json     |----+
+-------------------+    |
                         |     +-----------------------+     +------------------------+     +------------------------+
+-------------------+    ----> | Raw Ingestion & Python| --> | Persistent Storage     | --> | Downstream Analyst /   |
| products.parquet  |----+     | Pipeline / Profiling  |     | (PostgreSQL / Volumes) |     | Business Consumer      |
+-------------------+    |     +-----------------------+     +------------------------+     +------------------------+
                         |
+-------------------+    |
|   REST API        |----+
+-------------------+    |
                         |
+-------------------+    |
| PostgreSQL Source |----+
+-------------------+