# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os,json
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker
from mod.databases.db import engine

from mod.auth.loginHandler import LoginHandler
from mod.auth.logoutHandler import LogoutHandler

from mod.lostthing.GetLostHandler import GetLostHandler
from mod.lostthing.PubLostHandler import PubLostHandler


define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/herald/lost/login',LoginHandler),
            (r'/herald/lost/get',GetLostHandler),
            (r'/herald/lost/pub',PubLostHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            autoload=True,
            autoescape=None
        )
        

        tornado.web.Application.__init__(self, handlers,**settings)

        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html',hello='get')

    def post(self):
        ret = {'code':200,'content':'ok'}
        # self.set_header("Content-Type","text/json;charset=UTF-8")
        self.write(json.dumps(ret,ensure_ascii=False, indent=2))

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('404.html')
    def post(self):
        self.render('404.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
