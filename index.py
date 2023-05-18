import random
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/ask", methods=["GET"])
def ask():
  data = request.json
  data["options"]["parentMessageId"] = random.randrange(1, 1000000)
  
  response = requests.post("https://chatbot.theb.ai/api/chat-process", data = data)
  return response

app.run(host = "0.0.0.0", port = "80")