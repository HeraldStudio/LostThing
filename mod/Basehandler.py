# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from sqlalchemy.orm.exc import NoResultFound
from mod.databases.tables import Session

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    def on_finish(self):
        self.db.close()
    def get_current_user(self):
        cardnum = self.get_secure_cookie("cardnum")
        session = self.get_secure_cookie("session")
        if session != None and cardnum != None:
            try:
                status = self.db.query(Session).filter(Session.session_value == session,
                    Session.cardnum == cardnum).one()
                return status
            except NoResultFound:
                return False
        else:
            return False