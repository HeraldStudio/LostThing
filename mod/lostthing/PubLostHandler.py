# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
from ..databases.tables import User,Session,Thing
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from ..Basehandler import BaseHandler
import time

class PubLostHandler(BaseHandler):
    def get(self):
        # 渲染用于“发布”失物招领或者寻物启事的页面，需要先登录
        if not self.get_current_user():
            self.render("html\login.html")
        self.render("html/pub.html")
        

    def post(self):
        # 用于发布失物招领或者寻物启事，需要先登录，测试时不想登录先去掉了
        if not self.get_current_user():
            self.render("html/login.html")
        """
        用户发布失物招领或者寻物启事信息，成功则返回200
        参数：
            name 	物品名称
            dep 	物品描述
            contact	联系方式
            type	寻物启事则为1，失物招领则为2,其他情况或者不填默认为失物招领
        返回：
        """
        data = {}
        try:
            arg_name = self.get_argument("name")
            arg_dep = self.get_argument("dep")
            arg_contact = self.get_argument("contact")
            arg_type = self.get_argument("type")
            arg_time = time.time()
            if arg_type != '1':
                arg_type = 2
            thing = Thing(
                thing_name = arg_name,
                create_time = arg_time,
                description = arg_dep,
                contact = arg_contact,
                pub_type = arg_type,
                pub_user = 213130956
                )
            self.db.add(thing)
            self.db.commit()
            data["status"] = 200
            data["data"] = "Publish success."
            self.write(data)
        except Exception, e:
            print str(e)
            data["status"] = 403
            data["data"] = "Parameter error."
            self.db.rollback()
            self.write(data)



