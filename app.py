from flask import Flask, json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({'result': 'OK - healthy'}),
        status=200,
        mimetype='application/json'
            )
    app.logger.info('Status request successful!')
    return response


@app.route("/metrics")
def metrics():
    data = {'UserCount': 140, 'UserCountActive': 23}
    app.logger.info('Metrics request successful')
    return {'data': data}

def getUser():
    return {'user': 'admin'}

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
