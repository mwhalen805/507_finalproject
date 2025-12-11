## remove last 2 columns from comtrade_combined_clean.csv that got added on accident by clean_data
## saved to comtrade_combined_clean1.csv

import pandas as pd

chunksize = 100000
with pd.read_csv("comtrade_combined_clean.csv", chunksize=chunksize) as reader:
    for i, chunk in enumerate(reader):
        chunk = chunk.iloc[:, :-2]  # drop last two columns
        if i == 0:
            chunk.to_csv("comtrade_combined_clean1.csv", index=False)
        else:
            chunk.to_csv("comtrade_combined_clean1.csv", index=False, mode='a', header=False)