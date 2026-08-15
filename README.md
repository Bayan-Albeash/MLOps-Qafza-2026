# Olist Database Ingestion

## Objective

Load the Brazilian E-Commerce Public Dataset into a local PostgreSQL database using Docker, verify the database schema, and test SQL queries.

## Tools Used

- Docker Desktop
- PostgreSQL 17
- PowerShell
- SQL
- VS Code

## Dataset

Brazilian E-Commerce Public Dataset by Olist (Kaggle)

## Tables Loaded

- customers
- orders
- order_items
- order_payments
- order_reviews
- products
- sellers
- geolocation
- product_category_translation

## Row Counts

| Table | Rows |
|-------|------:|
| customers | 99,441 |
| orders | 99,441 |
| order_items | 112,650 |
| order_payments | 103,886 |
| order_reviews | 99,224 |
| products | 32,951 |
| sellers | 3,095 |
| geolocation | 1,000,163 |
| product_category_translation | 71 |

## Relationships

- orders.customer_id → customers.customer_id
- order_items.order_id → orders.order_id
- order_items.product_id → products.product_id
- order_items.seller_id → sellers.seller_id
- order_payments.order_id → orders.order_id
- order_reviews.order_id → orders.order_id

## Machine Learning Problem

The selected problem is **Late Delivery Classification**.

Target:

- Late: actual delivery date > estimated delivery date
- On Time: actual delivery date <= estimated delivery date

The actual delivery date is used only to create the target and should not be used as a model feature to avoid data leakage.

## Result

The database was successfully created, all CSV files were loaded into PostgreSQL, and SQL queries with joins were executed successfully.