import random
import requests
from flask import Flask
from flask import request, Response

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
  data = request.json
  data["options"]["parentMessageId"] = random.randrange(1, 1000000)
  
  response = requests.post("https://chatbot.theb.ai/api/chat-process", data = data)
  return Response(response)

app.run(host = "0.0.0.0", port = "80")
