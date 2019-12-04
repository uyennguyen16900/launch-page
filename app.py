from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Show the homepage"""
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    """Show menu"""
    return render_template('menu.html')

@app.route('/gallery')
def gallery_page():
    """Show gallery"""
    return render_template('gallery.html')

if __name__ == "__main__":
    app.run(debug=True)
