from flask import Flask
#dictionary
companies = {
         "toyota": 10213486,
         "volkswagen": 10126281,
         "hyundai": 7889538,
         "gm": 6971710
}
app = Flask(__name__)

@app.route("/company/<maker>")
def hello_world(maker): #keys are an input and values as an output
    return "{} has produced {} since it started operations".format(maker, str(companies[maker]))