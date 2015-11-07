# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
from ..databases.tables import User,Session,Thing
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from ..Basehandler import BaseHandler
import time

class GetLostHandler(BaseHandler):
    def get(self):
        # 渲染用于展示失物招领信息的页面，不需要登陆也能查看
        self.render("html/get.html")
        pass

    def post(self):
    	"""
        获取失物招领或者寻物启事信息，成功则返回列表
        参数：
        	day 	最近X天内的天数，如果不填默认为7天
            type	寻物启事则为1，失物招领则为2,其他情况或者不填默认为失物招领
        返回：
            status  状态码
            content 失物招领或者寻物启事信息列表

        示例返回:
        {
          "status": 200,
          "content": [
            {
              "dep": "于第三周在J8-201遗失，希望捡到的同学可以联系我",
              "pub_user": "213130956",
              "contact": "18795889958",
              "name": "Kindle",
              "time": "1446840721.657"
            },
            {
              "dep": "于第三周在J8-202遗失",
              "pub_user": "213130956",
              "contact": "18795889958",
              "name": "电源",
              "time": "1446840757.07"
            }
          ]
        }
        """
        data = {}
        content = []
        try:
            arg_day = self.get_argument("day")
            arg_type = self.get_argument("type")
            if arg_day == '':
                arg_day = 7
            if arg_type == '':
                arg_type = 2
            things = self.db.query(Thing).filter(Thing.pub_type == arg_type).all()
            for item in things:
                thing = {}
                thing["name"]=item.thing_name
                thing["time"]=item.create_time
                thing["dep"]=item.description
                thing["contact"]=item.contact
                thing["pub_user"]=item.pub_user
                if(float(item.create_time) >= (float(time.time())-float(arg_day)*3600*24)):
                    content.append(thing)
            data['status']=200
            data['content']=content
            self.write(data)
        except Exception ,e:
            print str(e)
            data["status"] = 403
            data["data"] = "Parameter error."
            self.db.rollback()
            self.write(data)

        


