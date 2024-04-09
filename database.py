from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv

load_dotenv()

# Use pymysql as the database driver
connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(connection_string)




#
# db_connection_string = "mysql+pymysql://avnadmin:AVNS_cDWv1klq_iGCO82-kAG@mysql-3488e08d-kakieosita-5890.a.aivencloud.com/defaultdb?charset=utf8mb4"
#
# engine = create_engine(db_connection_string)
