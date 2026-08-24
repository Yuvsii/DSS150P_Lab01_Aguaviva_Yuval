# Data Source Inventory

| Source Name | Format | Location | Description |
| :--- | :--- | :--- | :--- |
| **Customers** | CSV | `data/raw/customers.csv` | Primary customer demographic data, including IDs, names, emails, signup dates, and cities. |
| **Orders** | JSON | `data/raw/orders.json` | Transaction and order records containing item details, pricing, and customer references. |
| **Products** | Parquet | `data/raw/products.parquet` | Columnar storage file containing product catalog inventory, pricing, and categories. |
| **API Snapshot** | JSON | `data/raw/api_snapshot.json` | Captured response data pulled via REST API integration. |
| **Support Tickets** | PostgreSQL | Docker (`support_tickets` table) | Operational database table tracking customer support inquiries, priorities, status, and assigned agents. |