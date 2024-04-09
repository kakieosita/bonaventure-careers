from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        rows = result.fetchall()

        # Get column names
        column_names = result.keys()

        # Convert each row to a dictionary
        jobs = []
        for row in rows:
            row_dict = dict(zip(column_names, row))
            jobs.append(row_dict)
        return jobs


@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db())


if __name__ == '__main__':
    app.run(debug=True)
