from flask import Flask, render_template

# create a Flask application instance named app
app = Flask(__name__)

# connect the URL route "/" to the home() function
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)