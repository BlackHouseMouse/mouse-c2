from flask import Flask                  

app = Flask(__name__)                    

@app.route("/hello")                     
def hello():                             
    return "hi operator"

@app.route("/status")                     
def status():                             
    return "mouse in the house, last call 0s ago"    

@app.route("/info")
def info():
    return "Mouse c2 is a custom c2 built and maintained by BlackHouse Cyber!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
