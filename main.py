from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def get_keywords():
    data = request.get_json()
    query = data.get('query', '')
    keywords = query.lower().replace('find me','').replace('i want','').replace('show me','').strip()
    return jsonify({
        'keywords': keywords,
        'message': f"Got it! I'll find: {keywords}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
