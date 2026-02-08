# %%
import sqlite3
import pandas as pd

# %%
with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql(
        "select * from customers",
        con=connection
    )

df_customers.head(10)

# %%



