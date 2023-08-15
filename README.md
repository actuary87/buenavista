# Power BI loves DuckDB

This is a fork from https://github.com/jwills/buenavista project.

The aim is to get Power BI to connect to DuckDB through Postgres wire protocal which enables Direct Query on DuckDB. This makes the Power BI file is relatively small as the data resides in the DuckDB file and the queries are sent to it where only results are sent back to Power BI.

Only postgres_proxy.py method is used.

## How does this project work:
It is difficult to be able to process every valid SQL query and sends it DuckDB.

Many of the queries Power BI will send to a real Postgres server won't affect the result (it's not pulling any data).

In this project, the postgres_proxy.py sends those queries to a real Postgres Server to get a real response that makes Power BI happy.

On the other hand, any SQL query that pulls actual data is redirected to the DuckDB file set in buenavista\config.py file.

## To try the example I set in this repo, please do the following:

1. pip install -r requirements.txt (you can use a venv as well if you prefer)
2. Change the default values set in buenavista\config.py to the appropriate values
3. You can open the folder of the project in VSCode and click Ctrl+F5 to run it without debugging (or F5 for debugging mode)
4. Check the console for any errors: if you provide a wrong connection info to the real Postgres server you would see error messages instantly
5. If all is fine you should see Listening on 127.0.0.1:5433 (assuming you kept the default proxy port of 5433)
6. execute example\create_test_db_structure.sql on the real Postgres server after creating a database that matches the database name in the buenavista\config.py (test is the default value)
7. The real server won't have any data.
8. You can examine the two tables (customers and orders) in the DuckDB file using DBeaver (important: you have to close any connection to the DuckDB file though when you run the proxy server)
9. example\PowerBI_loves_DuckDB.pbix file is already configured to connect to the Proxy server localhost:5433 with credentials postgres/postgres, db = test and it has one visual that summarizes the orders count and sum per person
10. Try to make changes to the DuckDB (insert or update) and refresh Power BI to see the changes coming through
11. In some cases, it's better to kill the Proxy server and re run it again

I will try to post a tutorial on how to connect a new Power BI file to the proxy server/DuckDB with screenshots very soon.
