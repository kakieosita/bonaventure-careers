from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nigeria, Imo',
        'Salary': 'N  250,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Nigeria, Abuja',
        'Salary': 'N  500,000'
    },
    {
        'id': 3,
        'title': 'Software Developer',
        'location': 'Nigeria, Lagos',
        'Salary': 'N  600,000'
    },
    {
        'id': 4,
        'title': 'Front-end Engineer',
        'location': 'Remote',
        'Salary': 'N  300,000'
    }
]


@app.route('/')
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)
