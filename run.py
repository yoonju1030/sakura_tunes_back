from flask import Flask
from flask_restx import Api, Resource 
from flask_cors import CORS

app = Flask(__name__)
api = Api(app) 


@api.route('/hello') 
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}

if __name__ == "__main__":
    CORS(app, resources={r"*": {"origins": ["127.0.0.1:8081"]}}, supports_credentials=True)
    app.run(debug=True, host='0.0.0.0', port=80)