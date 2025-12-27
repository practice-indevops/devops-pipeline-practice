from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask inside Docker! \n"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so container port is reachable from host
    app.run(host="0.0.0.0", port=5000)

