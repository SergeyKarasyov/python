from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
from database_setup import RestaurantsDatabase
import cgi
from sqlalchemy import Column


class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161Los restaurants!</h1>"
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
                db = RestaurantsDatabase()
                restaurants = db.list_restaurants()
                for restaurant in restaurants:
                    output += "<h3> {} {}</h3> ".format(restaurant.name, restaurant.id)
                    output += "<a href='/restaurants/{0}/delete'>Delete</a> <a href='/restaurants/{0}/edit'>Edit</a>".format(restaurant.id)
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' accept-charset='utf-8' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output.encode('utf-8'))
                return

            if self.path.endswith("/edit"):
                print("edit start")
                restaurantIDPath = self.path.split("/")[2]
                db = RestaurantsDatabase()
                restaurant = db.get_restaurant_by_id(restaurantIDPath)
                if restaurant:
                    print("edit start2")
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>{}</h1>".format(restaurant.name)
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/{}/edit'>".format(restaurantIDPath)
                    output += "<input name = 'newRestaurantName' type = 'text' placeholder = '{}'> ".format(restaurant.name)
                    output += "<input type='submit' value='Rename'>"
                    output += "</form></body></html>"
                    self.wfile.write(output.encode('utf-8'))

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                db = RestaurantsDatabase()
                restaurant = db.get_restaurant_by_id(restaurantIDPath)
                if restaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>{}</h1>".format(restaurant.name)
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/{}/edit'>".format(restaurantIDPath)
                    output += "<input name = 'newRestaurantName' type = 'text' placeholder = '{}'> ".format(restaurant.name)
                    output += "<input type='submit' value='Delete'>"
                    output += "</form></body></html>"
                    self.wfile.write(output.encode('utf-8'))

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
            print(sys.exc_info()    )
        except:
            self.send_error(404, "{}".format(sys.exc_info()[0]))
            print(sys.exc_info()    )

    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurantID = self.path.split("/")[2]
                    db = RestaurantsDatabase()
                    restaurant = db.delete(restaurantID)
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
                    
                
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurant_name = fields.get('newRestaurantName')
                    messagecontent = restaurant_name[0].decode("utf-8")
                    db = RestaurantsDatabase()
                    db.add_restaurant(messagecontent)
                    print("created new restaurant {}".format(messagecontent))
                    for restaurant in db.list_restaurants():
                        print(restaurant.name)
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurantID = self.path.split("/")[2]
                    restaurant_name = fields.get('newRestaurantName')
                    messagecontent = restaurant_name[0].decode("utf-8")
                    print("start")
                    db = RestaurantsDatabase()
                    restaurant = db.update_by_id(restaurantID, restaurant_name)
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
                
            else:
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8"),
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                output = ""
                output += "<html><body>"
                output += " <h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode('utf-8'))
                print(output)
        except:
            self.send_error(404, "{}".format(sys.exc_info()[0]))
            print(sys.exc_info()    )


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    main()
