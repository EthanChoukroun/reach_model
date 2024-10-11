from flask import Flask, request, jsonify
from pydantic import BaseModel
from typing import List
import main
import transactions

# app = FastAPI()
app = Flask(__name__)

class Transaction(BaseModel):
    date: str
    amount: float
    name: str

# @app.get("/")
@app.route("/", methods=['GET'])
def read_root():
    return jsonify({"Hello": "World"})

@app.route("/calculate_budget", methods=['POST'])
def calculate_budget():
    transactions = request.json.get('transactions')
    if not transactions:
        return jsonify({"error": "No transactions provided"}), 400
    data = main.create_datasets(transactions)
    smart_budget = main.calculate_smart_budget(data)
    return jsonify({f"Your smart budget is ${smart_budget}"})


if __name__ == "__main__":
    app.run(host="134.122.123.99", port=5000)












