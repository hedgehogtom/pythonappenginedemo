# V1: Google App Engine for Python 2.7
#     1. Hello, World demo

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')      

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug = True)
