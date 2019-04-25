from flask import Flask
from avito import title

app = Flask(__name__)

@app.route("/")
def hello():
    print (title) 



if __name__=="__main__":
    app.run()