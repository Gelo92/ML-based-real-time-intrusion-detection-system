#gothic-style-406819.bq_vpcflows.v
import os
import pathlib
from flask import Flask, render_template
from google.cloud import bigquery
import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Google Login App")
app.secret_key = "CodeSpecialist.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "929663547058-c85bv36naqhhvo1h2kpl5dkn8i6oh3hh.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

app = Flask(__name__)

# Replace 'your_project' and 'your_dataset.your_table' with your actual project and table names
project_id = 'gothic-style-406819'
table_id = 'bq_vpcflows.v'

# Set up BigQuery client
client = bigquery.Client(project=project_id)

# Define a route to display the selected fields in HTML
@app.route('/')
def show_table():
    # Specify the fields you want to retrieve
    fields = ['timestamp', 'src_ip', 'dest_ip', 'bytes_sent', 'src_port', 'dest_port',  'protocol', 'packets_sent']

    # Construct the SELECT statement
    select_fields = ', '.join(fields)
    query = f'SELECT {select_fields} FROM `{project_id}.{table_id}`'

    # Fetch data from BigQuery table
    query_job = client.query(query)
    rows = query_job.result()

    # Convert rows to a list of dictionaries for easy rendering in HTML
    data = [dict(row.items()) for row in rows]

    # Render HTML template with the selected fields
    return render_template('table.html', data=data, fields=fields)

if __name__ == '__main__':
    app.run(debug=True)
