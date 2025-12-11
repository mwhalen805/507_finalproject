import pandas as pd

input_csv = "comtrade_combined_clean1.csv"
output_json = "comtrade_data.json"
columns_to_drop = ['datasetCode', 'typeCode', 'freqCode', 'refYear', 'refMonth', 'period', 'partner2Code', 'classificationSearchCode', 'classificationCode', 'isOriginalClassification', 'customsCode', 'mosCode', 'motCode', 'qtyUnitCode', 'isQtyEstimated', 'altQtyUnitCode', 'altQty', 'isAltQtyEstimated', 'isNetWgtEstimated', 'isGrossWgtEstimated', 'CIFValue', 'FOBValue', 'primaryValue', 'legacyEstimationFlag', 'isReported', 'isAggregate'] 
chunk_size = 100000

with open(output_json, "w") as json_file:
    json_file.write("[\n")  # start JSON array

    first_chunk = True
    for chunk in pd.read_csv(input_csv, chunksize=chunk_size):
        chunk = chunk.drop(columns=columns_to_drop, errors='ignore')
        
        # Convert chunk to JSON array string (list of dicts)
        chunk_json = chunk.to_json(orient='records')

        # Remove the surrounding brackets from chunk JSON string
        chunk_json = chunk_json[1:-1]

        if not first_chunk:
            json_file.write(",\n")  # comma separator between chunks
        else:
            first_chunk = False

        json_file.write(chunk_json)

    json_file.write("\n]")  # end JSON array