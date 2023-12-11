from flask import Flask

# Instantiate Flask application
app = Flask(__name__)

# Create route for root (home) page of website
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

# Create route for about page
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
	app.run(debug=True)
