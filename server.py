from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForPreTraining
from dotenv import load_dotenv
import openai
from openai import OpenAI
import os

load_dotenv()

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModelForPreTraining.from_pretrained("nlpaueb/legal-bert-base-uncased",)
app = Flask(__name__)

CORS(app)

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"), organization = "os.getenv('OPEN_AI_ORG')")
def get_response(query_text):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": query_text
            }
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message.content

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    chat = data.get("messages", [])
    if len(chat) == 0:
        return Response(status=400)
    query_text = chat[-1]["content"]
    tokenized_query_text = tokenizer(query_text, return_tensors='pt', truncation=True, max_length=500)
    model(**tokenized_query_text).prediction_logits.shape
    response = get_response(query_text)
    if isinstance(response, dict) and "error" in response:
        return jsonify(response), 500  # Return the error response with 500 status
    
    return jsonify({"reply": response}) 
    


app.run()