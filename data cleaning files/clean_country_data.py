import csv
import json

country_name_to_code = {}

with open("countries.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["name"].strip()
        code = row["country-code"].lstrip("0")  # Remove leading zeros for consistency
        if code == "":
            continue  # skip empty codes
        country_name_to_code[name] = code  # store as string without leading zeros

# Optional: save to JSON
with open("country_name_to_code.json", "w", encoding="utf-8") as f:
    json.dump(country_name_to_code, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(country_name_to_code)} countries.")
