from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from medibot import give_response
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    msg = request.form.get("Body", "")
    sender = request.form.get("From", "")
    phone_number = sender.replace("whatsapp:", "")
    answer=give_response(msg,phone_number)
    response = MessagingResponse()
    message = Message()
    message.body(answer)
    response.append(message)
    return str(response)

@app.route("/whatsapp", methods=["GET"])
def test():
    return "Bot is running fine!"

if __name__ == "__main__":
    app.run(debug=True)
