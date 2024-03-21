import pandas as pd

df = pd.read_csv('products_export.csv')

df['Title'] = df['Title'].replace("[a-z A-Z]+ ?- ?", "", regex=True).str.upper()

print(df["Title"])