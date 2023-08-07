#Coded by Techie Harpreet on 05th Aug 2023
from flask import Flask, request, jsonify
from inshorts import getNews,getHindiNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "Techie Harpreet"
CORS(app)

@app.route('/news')
def news():
    if request.method == 'GET':
        category = request.args.get("category")
        if not category:
            return jsonify({
                "error": "please add category in query params"
            }), 404
        return jsonify(getNews(category)), 200
    
@app.route('/news-hin')
def newsHindi():
    if request.method == 'GET':
        return jsonify(getHindiNews(request.args.get('category')))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
