<<<<<<< HEAD

from flask import Flask, request

# creating flask app using flask function
app = Flask(__name__)

# creating api route
@app.route('/api', methods=['POST'])
def say_hello():
    data = request.get_json(force=True)
    name = data['name']
    return ("hello {0}".format(name))

if __name__ == '__main__':
=======

from flask import Flask, request

# creating flask app using flask function
app = Flask(__name__)

# creating api route
@app.route('/api', methods=['POST'])
def say_hello():
    data = request.get_json(force=True)
    name = data['name']
    return ("hello {0}".format(name))

if __name__ == '__main__':
>>>>>>> 8aef0f615c8f1ec20517ade89dd31e97478619f9
    app.run(port=10001, debug=True)