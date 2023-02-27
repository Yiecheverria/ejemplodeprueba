import os

from config import dabase_config
from dotenv import load_dotenv
from migration import author_migration
from flask import Flask
from rest import author_rest

load_dotenv()
app = Flask(__name__)
if __name__ == '__main__':
    # connect database
    connection = dabase_config.connection()
    # migration
    author_migration.migrate(connection)
    # define rules
    app.add_url_rule("/authors", view_func=author_rest.AuthorRest.as_view('author'))
    app.add_url_rule("/authors/<id>", view_func=author_rest.AuthorRest.as_view('author_id'))
    # run server
    app.run(debug=True, host='0.0.0.0', port=os.getenv('SERVER_PORT'))
