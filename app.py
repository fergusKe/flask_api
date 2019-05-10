from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('quation')

class ChatBot(Resource):
    def get(self):
        return {
          'answer': 'get answer'
        }, 200

    def post(self):
        args = parser.parse_args()
        name = args['name']
        quation = args['quation']
        answer = {
          'answer': name + 'your quation is' + quation + ', my answer is ...'
        }
        return answer, 200

api.add_resource(ChatBot, '/chatbot')

if __name__ == '__main__':
    app.run(debug=True)