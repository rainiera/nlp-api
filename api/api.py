import sys
import logging
from flask import Flask, request
from models.pos_tagger import pos_tag_json


app = Flask(__name__)
# So Flask errors log to stdout - nice for deploy logs and CI
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return "Welcome to the NLP API, v-0.1. You'll need to specify a service, " \
           "a key passed through GET, and data sent through POST."


@app.route('/<str:service>?key=<str:api_key>', methods=['POST'])
def get_handler(service, api_key):
    if api_key_valid(api_key):
        post = request.form
        dispatch(service, post, api_key)
    else:
        return "401 Unauthorized"


def dispatch(service, post, api_key):
    """Dispatch the service along with the post dict and api_key
    api_key - can use for stats and possibly rate-limiting
    """
    if service == "debug":
        return "You used this API key: %s" % api_key
    elif service == "postokenize":
        return post
        # return pos_tag()


def api_key_valid(api_key):
    """Check if the API key is in the database
    For now this is especially left up to the user how they'll
    """
    # return api_key in db.query(keydb)
    return True


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    if len(sys.argv) < 1 or not is_int(sys.argv[1]):
        sys.exit('Usage: `python api.py PORT_NUMBER`')
    app.run(debug=True, port=int(sys.argv[1]))
