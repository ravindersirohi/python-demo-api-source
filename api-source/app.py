from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health-check')
def health():
    return "App is up and running."