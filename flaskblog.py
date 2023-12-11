from flask import Flask, render_template

# Instantiate Flask application
app = Flask(__name__)

posts = [
    {
        'author': 'Kyle Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# Create route for root (home) page of website
@app.route("/")
@app.route("/home")
def home():
    # We will have access to 'posts' variable within our template
    return render_template('home.html', posts=posts)

# Create route for about page
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
