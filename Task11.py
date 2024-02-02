# 2887. Fill Missing Data
# Write a solution to fill in the missing value as 0 in the quantity column.
# 
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(int('0'), inplace=True)
    return products