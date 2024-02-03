# 176. Second Highest Salary
# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
# 
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    r = employee['salary'].drop_duplicates().nlargest(2)
    if len(r) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    result = r.iloc[-1]
    return pd.DataFrame({'SecondHighestSalary': [result]})