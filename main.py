from os import getcwdu
import random
import cherrypy

from web_base import WebBase
from emoji import Emoji
from kaomoji import Kaomoji


class Emoticons(object, WebBase):
    def __init__(self):
        self.kaomoji = Kaomoji(self)
        self.emoji = Emoji(self)


    @cherrypy.expose
    def index(self):
        # HACK!
        raise cherrypy.HTTPRedirect('/kaomoji')


    @cherrypy.expose
    def about(self):
        return self._template('about.html', {})



if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0'
    })
    cherrypy.quickstart(Emoticons(), config={
       '/static':
       {
           'tools.staticdir.on': True,
           'tools.staticdir.dir': getcwdu()+'/static'
       }
    })
