from flask import Flask, request, jsonify
from strawberry.flask.views import GraphQLView
import strawberry
from typing import List

from api.schema import schema

# Initialize the Flask app
app = Flask(__name__)

# Add GraphQL view
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema)
)


if __name__ == "__main__":
    app.run(debug=True)
