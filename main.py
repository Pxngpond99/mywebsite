from flask import Flask, render_template

from views import accounts

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main/index.html")


if __name__ == "__main__":
    app.register_blueprint(accounts.bp)
    app.run(debug=True)
