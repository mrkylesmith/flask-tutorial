from flask import Flask

# Instantiate Flask application
app = Flask(__name__)

# Create route for root (home) page of website
@app.route("/")
def hello():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
	app.run(debug=True)
