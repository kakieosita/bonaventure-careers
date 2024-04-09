from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv

load_dotenv()

# Use pymysql as the database driver
connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(connection_string)


# def load_job_from_db(id):
#     with engine.connect() as conn:
#         result = conn.execute(
#             text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
#         )
#         rows = result.fetchall()
#
#         # Get column names
#         column_names = result.keys()
#         job = []
#         if len(rows) == 0:
#             return None
#         else:
#             row_dict = dict(zip(column_names, rows[0]))
#             job.append(row_dict)
#             return job

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
        )
        row = result.fetchone()  # Fetch a single row

        if row is None:
            return None
        else:
            # Fetch column names
            column_names = result.keys()
            # Construct dictionary using column names and row values
            job = dict(zip(column_names, row))
            return job


