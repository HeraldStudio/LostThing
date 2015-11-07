#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import engine, Base
# from tables import User,Bussiness
from tables import User,Cookie,PhoneCode,Business,Business_Order,Share,FileTag
try:
    Base.metadata.create_all(engine) #create all of Class which belonged to Base Class
except Exception,e:
    print str(e)