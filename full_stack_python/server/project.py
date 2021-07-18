from flask import Flask
from database_setup import RestaurantsDatabase

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    output = ""
    db = RestaurantsDatabase()
    restaurants = db.list_restaurants()
    for restaurant in restaurants:
        output += restaurant.name
        output += '</br>'
    print(output)
    return output   

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
