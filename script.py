import pandas as pd
""" 
to do - add automated tags
find a way to get rid of size and color params at end of text
grab variant names and filter by them
"""

df = pd.read_csv('products_export.csv')

print(df)


new_df = pd.DataFrame({"Title": "my new row"}, index=[0])

df = pd.concat([df,new_df], ignore_index=True)

df["Title"] = df["Title"].astype(str)
#dfFiltered = df["Title"].str.contains("[a-z A-Z]+ ?- ?", regex=True)
dfEditManually = df[~df["Title"].str.contains("[a-z A-Z]+ ?- ?", regex=True)]




# dfOthers = df[~dfFiltered(df)]

df['Title'] = df['Title'].replace("[a-z A-Z]+ ?- ?", "", regex=True).str.upper()

print(dfEditManually)