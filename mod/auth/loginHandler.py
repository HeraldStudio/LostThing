# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
from ..databases.tables import User,Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
import uuid,re
import time
import traceback
import uuid
from ..Basehandler import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render("html/login.html")

    def post(self):
        """
        用户登录，成功则返回200，并且设置cookie
        参数：
            cardnum
            password
        返回：
            status  状态码
            data    返回数据
        示例返回
        {
          "status": 200,
          "data": "Login successfully."
        }
        """
        data = {}
        try:  
            cardnum = self.get_argument('cardnum')
            password = self.get_argument('password')
            user = self.db.query(User).filter(User.cardnum == cardnum).first()
            if password == user.password:
                uuid_session = str(uuid.uuid4())
                create_time = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
                data_session = Session(session_value = uuid_session,cardnum = cardnum,create_time=create_time)
                self.db.add(data_session)
                self.db.commit()
                self.set_secure_cookie("session",uuid_session)
                self.set_secure_cookie("cardnum",str(user.cardnum))
                data["status"] = 200
                data["data"] = "Login successfully."
                self.write(data)
                # self.redirect("/herald/lost/get")
            else:
                data["status"] = 403
                data["data"] = "Password wrong."
        except Exception ,e:
            print str(e)
            data["status"] = 403
            data["data"] = "Login failed."
            self.db.rollback()
            self.write(data)