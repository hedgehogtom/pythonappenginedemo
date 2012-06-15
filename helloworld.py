import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        self.response.out.write('Hi Tom this is Avner!')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug = True)