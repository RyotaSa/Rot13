import os

import jinja2
import webapp2
import string



from google.appengine.ext import db

template_dir = os.path.abspath(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                 autoescape = True)

def render_str(template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render('rot13.html')
    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')

        self.render('rot13.html', text = rot13)

app = webapp2.WSGIApplication([('/', MainPage),], debug = True)
