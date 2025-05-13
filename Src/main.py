# src/main.py

from flask import Flask, request, jsonify
from validator import validate_hsn

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()

    # Support ADK structure
    parameters = data.get("parameters", {})
    codes = parameters.get("HSNCode", [])

    results = []
    for code in codes:
        result = validate_hsn(code)
        results.append(result)

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)