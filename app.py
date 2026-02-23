from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Route for the "About Me" link
@app.route('/about')
def about():
    return "<h1>About Me Page</h1><p>Coming soon...</p>"

# Route for the "Personal Projects" link
@app.route('/projects')
def projects():
    return "<h1>Projects Page</h1><p>Coming soon...</p>"

if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you save changes
    app.run(debug=True, port=5000)
