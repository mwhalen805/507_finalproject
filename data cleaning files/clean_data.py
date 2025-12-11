import pandas as pd
import glob
import os
from io import StringIO

folder_path = "/Users/monicawhalen/Desktop/SI 507/Final Project"
output_path = os.path.join(folder_path, "comtrade_combined_clean.csv")
        
clean_lines = []

# remove trailing commas 
with open(os.path.join(folder_path, "country_codes.csv"), "r", encoding="latin-1") as f:
    lines = [line.rstrip(",\n") for line in f] 

max_commas = max(line.count(",") for line in lines)
normalized_lines = []

# add extra commas to lines missing a column
for line in lines:
    missing = max_commas - line.count(",")
    normalized_lines.append(line + ("," * missing) + "\n")

cleaned_text = "".join(normalized_lines)

country_ref = pd.read_csv(StringIO(cleaned_text), sep=",", quotechar='"', engine="python")

country_ref = country_ref[['text', 'reporterCode']] # just need country name (text) and reporter code columns

first_write = True

for file in glob.glob(os.path.join(folder_path, "*.txt")):
    print(f"Processing {file}...")
    for chunk in pd.read_csv(file, sep='\t', chunksize=100000, low_memory=False):
        # remove world, free zones, and unspecified zones for partners (only keep partners that are countries)
        chunk = chunk[(chunk['partnerCode'] != 0) & (chunk['partnerCode'] != 97) & (chunk['partnerCode'] != 470)]
        # remove aggregated areas
        chunk = chunk[chunk['isAggregate'] == 0]
        
        # Map codes to names
        if 'reporterCode' in chunk.columns:
            chunk = chunk.merge(
                country_ref, left_on='reporterCode', right_on='reporterCode', how='left'
            ).rename(columns={'country': 'reporterName'})

        if 'partnerCode' in chunk.columns:
            chunk = chunk.merge(
                country_ref, left_on='reporterCode', right_on='reporterCode', how='left'
            ).rename(columns={'country': 'reporterName'})

        ### The mapping did not work correctly but everything else is fine
        
        
        # Save incrementally
        chunk.to_csv(output_path, mode='a', index=False, header=first_write)
        first_write = False

print(f"Output saved to: {output_path}")


