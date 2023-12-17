# flask-tutorial
Following this [Flask Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

# Install Flask
```bash
pip3 install flask
```

# Run App
```python
export FLASK_APP=flaskblog.py
flask run
```

# Or, we can put this into the flaskblog.py
```python
if __name__ == '__main__':
	app.run(debug=True)
```


# Routes:

- You can return HTML directly from a route, if you wanted.
Eg)
```python
@app.route('/home')
def home():
	return '''<!doctype html>
	<html>
	'''
```
**However this would get bloated very fast**
Instead use templates!

## Templates
- Create a `templates` subdirectory within your project.

Import the `render_template` function:
```python
from flask import Flask, render_template
```
Now we can render static html pages from the `templates` directory using `render_template()`

### Template Inheritance
- Can be used to reduce repetative code into reusable components, that HTML documents can inherit from.
- An example of this can be seen in `templates/layout.html`, which is the parent template that will be inherited.

		- Any template that inherits from `layout.html` can override the content block with it's own data.


## Styling with Bootstrap
- In this tutorial, we add Bootstrap using a CDN (Content Delivery Network)
- Used Bootstrap starter template here: [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/), which is a different version of Bootstrap then the tutorial used.


### Styling Snippits
- At this point, the tutorial shows some examples of styling a webpage using the snippits provided here: [https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets)
-
- I used the navigation style in [navigation.html](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/snippets/navigation.html) and the [main.html](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/snippets/main.html) snippit.

# Static Files
- Flask expects any static files (such as static JavaScript or CSS files) to be located within a `static/` directory.

- I have added a `main.css` file, which the tutorial provided and instructed to place within the `static` directory.
Therefore the current directory structure now looks like this:
```bash
.
├── README.md
├── __pycache__
│   └── flaskblog.cpython-38.pyc
├── flaskblog.py
├── static
│   └── main.css
└── templates
    ├── about.html
    ├── home.html
    └── layout.html

3 directories, 7 files
```

### Flask url_for function

We can use the `url_for` function to tell our HTML pages where to look for static files.
Example:
```html
<!-- Use Flask url_for to give location of static css file, within the static directory, named 'main.css' -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}">
```

- Adding another snippit from [article.html](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/snippets/article.html), within our home page body content, to replace what we had previously.
	

# Forms and User Input
- Part 3 of the tutorial

Create a file called `forms.py`.  For sake of modularity and readability, best to create a separate file for this. We can easily add additional forms to this file.

We will use this Flask extension called [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/), which allows us to write forms as python classes, instead of HTML forms. Then the extension will automatically convert the classes to forms within our template.

Example form class:
```python
class RegistrationForm(FlaskForm):
```
Within this form class, we can have our fields be imported classes.

We will import the following to help us with this:
```python
from wtforms import StringField
```
`StringField` will help us with both our `username` and `email` fields.

Also, validators will help us protect against bad user input such as:
- Null username -> We will use the `DataRequired` validator for this.
- username outside of required length (too short or too long) -> We will use the `Length` validator for this.
- email -> We can use the `Email` validator

We will need a different, specialized form class for the password field, so we can import the following:
```python
from wtforms import PasswordField
```
