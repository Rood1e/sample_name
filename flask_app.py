from flask import Flask, request
from alice_sdk import *
from main_fuction import *

app = Flask(__name__)
session_storage = {}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/", methods=["POST"])
def main():
    alice_request = AliceRequest(request.json)
    alice_response = AliceResponse(alice_request)
    alice_response, session_storage[alice_request.user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(alice_request.user_id)
    )
    return alice_response.dumps()


if __name__ == '__main__':
    app.run()

