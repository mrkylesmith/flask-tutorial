from flask import Flask, render_template, url_for

# Instantiate Flask application
app = Flask(__name__)

posts = [
    {
        'author': 'Kyle Smith',
        'title': 'What is Supercomputing?',
        'content': 'First post content',
        'date_posted': 'September 16, 2023'
    },
    {
        'author': 'Francisco Gutierrez',
        'title': 'Rocky Linux!',
        'content': 'Second post content',
        'date_posted': 'October 21, 2023'
    },
    {
        'author': 'Khai Vu',
        'title': 'Everything Networking',
        'content': 'Third post content',
        'date_posted': 'November 11, 2023'
    },
    {
        'author': 'Ben Sterling',
        'title': 'The Rust Programming Language',
        'content': 'Fourth post content',
        'date_posted': 'December 5, 2023'
    }
]

# Create route for root (home) page of website
@app.route("/")
@app.route("/home")
def home():
    # We will have access to 'posts' variable within our template
    # Sort the posts by date written (most recent first)
    sorted_by_date = sorted(posts, key=lambda key: key['date_posted'])
    return render_template('home.html', posts=sorted_by_date)

# Create route for about page
@app.route("/about")
def about():
    # Pass title to about page
    return render_template('about.html', title="About")

if __name__ == '__main__':
	app.run(debug=True, port=5000)


