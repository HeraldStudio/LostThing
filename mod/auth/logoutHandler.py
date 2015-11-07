# -*- coding: utf-8 -*-
#!/usr/bin/env python
from ..Basehandler import BaseHandler
import json
#/auth/logout
class LogoutHandler(BaseHandler):
    # @tornado.web.authenticated
    def delete(self):
        pass