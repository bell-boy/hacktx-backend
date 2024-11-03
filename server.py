from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForPretraining

tokenizer = AutoTokenizer.from_pretrained("nlpauee/legal-bert-base-uncased")
model = AutoModelForPretraining.from_pretrained("nlpauee/legal-bert-base-uncased", device_map="auto")
app = Flask(__name__)

CORS(app)

@app.route("/query", methods=["get"])
def query():
    data = request.json
    chat = data.get("messages", [])
    if len(chat) == 0:
        return Response(status=400)
    query_text = chat[-1]["content"]
    tokenized_query_text = tokenizer(query_text, return_tensors='pt', truncation=True, max_length=500)
    


app.run()