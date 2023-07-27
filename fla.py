from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to python flask app pipeline"


app.run(host="0.0.0.0", port=4000)
