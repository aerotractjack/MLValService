from flask import Flask, request, jsonify
from flask_executor import Executor
from flasgger import Swagger
import sys
from docs import template, swag_mlval
from MLVal import MLValReport, integration

app = Flask(__name__)
executor = Executor(app)
swagger = Swagger(app, template=template)

def log(msg):
    print(msg)
    sys.stdout.flush()

@app.route("/mlval", methods=['POST'])
@swag_mlval
def mlval():
    '''
    API endpoint to submit ML validation calculation requests for predictions
    '''
    return jsonify("mlval!"), 200

if __name__ == "__main__":
    app.run(port=7114, host="0.0.0.0")