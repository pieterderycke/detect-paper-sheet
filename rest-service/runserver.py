"""
This script runs the rest_service application using a development server.
"""

from os import environ
from flask import render_template
import connexion
from connexion.resolver import RestyResolver

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml', resolver=RestyResolver('api'))
app.run(port=8080)

#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT)
