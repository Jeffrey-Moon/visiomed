from flask import Flask

app = Flask(__name__)


@app.route('/')
def flask():
    
   return "hi"


if __name__ == "__main__":
   app.run(host = "172.30.1.53", port = "8090")