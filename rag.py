import iris
import os
from dotenv import load_dotenv

load_dotenv()


username='demo'
password='iris'
port='1972'
namespace='USER'
hostname=os.getenv('IRIS_HOSTNAME', 'localhost')
CONNECTION_STRING = f"{hostname}:{port}/{namespace}"

conn = iris.connect(CONNECTION_STRING, username, password)
cursor = conn.cursor()