from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        name = request.values['name']
        quation = request.values['quation']
        answer = {
          'answer': name + 'your quation is' + quation + ', my answer is ...'
        }
        return jsonify(answer), 200
    else:
        answer = {
          'answer': 'get answer'
        }
        return jsonify(answer), 200

if __name__ == '__main__':
    app.run(debug=True)