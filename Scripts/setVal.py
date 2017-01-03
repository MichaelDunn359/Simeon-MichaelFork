from google.appengine.ext import webapp

class MyRequestHandler(webapp.RequestHandler):
   def get(self):
      self.response.out.write(self.request.get('val'));