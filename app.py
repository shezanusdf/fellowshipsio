from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.environ.get("DATABASE_PATH", "database.db")

@app.route("/")
def home():

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM fellowships WHERE type IN (?,?,?)", ("fellowship","accelerator","venture capital"))

    fellowships = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        fellowships = fellowships
        )

@app.route("/grants")
def grants():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM fellowships WHERE type = ?", ("grant",))

    fellowships = cursor.fetchall()

    connection.close()

    return render_template(
        "grants.html",
        fellowships = fellowships
        )

@app.route("/residencies")
def residencies():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM fellowships WHERE type = ?", ("residency",))

    fellowships = cursor.fetchall()

    connection.close()

    return render_template(
        "residencies.html",
        fellowships = fellowships
        )


if __name__ == "__main__":
    app.run(debug=True)