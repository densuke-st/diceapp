from bottle import run,route, response
from json import dumps
from random import randint

@route("/v2/<d:int>")
@route("/v1/")
@route("/")
def roll(d = 1):
    rolls = []
    for i in range(d):
        rolls.append(randint(1,6))
    data = {
        'roll': sum(rolls),
        'dices': len(rolls),
        'values': rolls
    }
    response.set_header('Content-Type', 'application/json')
    return dumps(data)

if __name__ == "__main__":
    run(host="0.0.0.0", port=80, debug=None, quiet=True)
