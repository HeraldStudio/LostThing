#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float 
from sqlalchemy.orm import relationship,backref
from db import engine,Base

class User(Base):
	__tablename__ = 'user'
	cardnum = Column(String,primary_key=True)
	password = Column(String)
	number = Column(VARCHAR)


class Session(Base):
	__tablename__ = 'sessions'
	session_id = Column(Integer,primary_key=True)
	session_value = Column(String)
	create_time = Column(VARCHAR)
	cardnum = Column(String)

class Thing(Base):
	__tablename__ = 'thing'
	thing_id = Column(Integer,primary_key=True)
	thing_name = Column(String)
	create_time = Column(VARCHAR)
	description = Column(VARCHAR)
	contact = Column(VARCHAR)
	pub_type = Column(VARCHAR)
	pub_user = Column(VARCHAR)





	

	


