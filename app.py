from bottle import run,route, response
from json import dumps
from random import randint

@route("/v1/")
@route("/")
def roll():
    num = randint(1,6)
    data = {
        'roll': num
    }
    response.set_header('Content-Type', 'application/json')
    return dumps(data)

if __name__ == "__main__":
    run(host="0.0.0.0", port=80, debug=None, quiet=True)
