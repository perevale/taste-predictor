from flask import Flask, request
from flask_restx import Api, Resource
import random


app = Flask(__name__)
swagger = Api(app=app,
              version="1.0",
              title="Taste Predictor",
              description="")

api = swagger.namespace("predictions", description='')

@api.route("/predict", methods=['GET'])
class Taster(Resource):
	@swagger.doc(responses={200: 'OK'})
	def get(self):
		params = request.args.to_dict()
		return taste(**params)

def taste(*args, **kwargs):
	return random.randint(0, 1)

if __name__ == '__main__':
    app.run(debug=True)