import json
from flask import Flask, jsonify, request
from trade_graph import TradeGraph
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

with open("country_name_to_code.json") as f:
    name_to_code = json.load(f)

# create code to name dictionary
code_to_name = {v: k for k, v in name_to_code.items()}

with open("comtrade_data.json") as f:
    trade_data = json.load(f)

graph = TradeGraph()
graph.load_trade_data(trade_data)


# Helper functions
def normalize_country_name(name):
    return name.strip().title()

def code_to_country(code):
    return code_to_name.get(code, f"Unknown ({code})")


# API: Get trading partners
@app.get("/partners/<code>")
def get_partners(code):

    code = code.strip()
    # Check name exists
    if code not in code_to_name:
        return jsonify({"Error": f"Unknown country code'{code}'"}), 404

    if code not in graph.graph:
        return jsonify({"Error": f"No trade data for {code}"}), 404

    partner_codes = graph.graph[code]

    return jsonify({
        "country": code,
        "partners": list(partner_codes)
    })

# API: sort countries by most trade partners
@app.get("/top-countries")
def get_top_countries():
    limit = int(request.args.get("limit", 20))
    result = graph.number_of_connections()
    # Return top N
    top_countries = result[:limit]
    # Convert codes to names for display
    return jsonify([
        {"code": code, "name": code_to_name[code], "num_partners": num}
        for code, num in top_countries
        if code in code_to_name
    ])

# API: List all countries
@app.get("/countries")
def list_countries():
    return jsonify(sorted(name_to_code.keys()))

if __name__ == "__main__":
    app.run(debug=True)