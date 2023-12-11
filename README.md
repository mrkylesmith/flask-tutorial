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

NOTE: Flask uses jinja2 templating engine.









