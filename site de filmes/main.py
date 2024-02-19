from flask import Flask 
from routes.home import home_route
from routes.filmes import filmes_route
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(filmes_route,url_prefix='/filmes')

app.run(debug=True)