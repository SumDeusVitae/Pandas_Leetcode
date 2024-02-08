# 1795. Rearrange Products Table
# Write a solution to rearrange the Products table so that each row has (product_id, store, price). 
# If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
# Return the result table in any order.
# 
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars=['product_id'], var_name = 'store', value_name = 'price').dropna()