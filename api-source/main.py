# import os
# from flask import Flask,render_template, jsonify, request

# app = Flask(__name__)

# static_list = []

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/health-check')
# def health_check():
#     return "Hello, I am healthy!"

# @app.route('/list-items')
# def list_items():
#     return jsonify(static_list)

# @app.route('/add-item', methods=['POST'])
# def add_item():
#     name = request.json['name']
#     if name is not None and name !='':
#         static_list.append({"name":name})
#         return "Item added into the list!"
#     else:
#         return "Unable to add item!"

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
#     # app.run(debug=True)

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
