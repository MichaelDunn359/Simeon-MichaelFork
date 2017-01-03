import webapp2
import codecs

class Page(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')
        print "loading can"
        page = codecs.open("fabrictest.htm", 'r', 'utf-8')
        self.response.write(page.read())

app = webapp2.WSGIApplication([
    ('/', Page),
], debug=True)
