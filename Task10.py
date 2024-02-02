# 2886. Change Data Type
# Write a solution to correct the errors:
# The grade column is stored as floats, convert it to integers.
#
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade':int})
    