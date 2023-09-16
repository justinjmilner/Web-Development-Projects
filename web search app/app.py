from flask import Flask, render_template

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/advanced_search')
def advanced():
    return render_template('advanced.html')

@app.route('/images')
def images():
    return render_template('images.html')

if __name__ == '__main__':
    app.run(debug=True)