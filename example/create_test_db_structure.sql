-- Create a new database called 'test' on the real server then execute the following sql script
-- No need to import any data into the real Postgres server as all data will be pulled from the DuckDB file
CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS public.customers (customer_id INTEGER, customer_name TEXT);

CREATE TABLE IF NOT EXISTS public.orders (order_id INTEGER, customer_id INTEGER, order_amount DECIMAL(18,2));
