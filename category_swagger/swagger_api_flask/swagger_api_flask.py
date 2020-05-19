try:
    from flask import Flask, request
    from flask_restful import Resource, Api
    
    from flask_limiter.util import get_remote_address
    from flask_limiter import Limiter

    from flasgger import Swagger
    from flasgger.utils import swag_from
    from flask_restful_swagger import swagger

except Exception as e:
    print("Some modules are missing:: {}".format(e))


app = Flask(__name__)
api = Api(app)

limiter = Limiter(app, key_func=get_remote_address)
limiter.init_app(app)

api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/doc')

class MyApi(Resource):

    decorators = [limiter.limit("2/day")]
    @swagger.model
    @swagger.operation(notes='some really good notes')
    def get(self, zip):
        return {
            'Response': 200,
            'Data': zip
        }

api.add_resource(MyApi, '/weather/<string:zip>')


if __name__ == "__main__":
    app.run(debug=True)