#从flask包里导入Flask类
from flask import Flask
from config import Config #从config模块里导入COnfig类
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app) #数据库对象
migrate=Migrate(app,db) #迁移引擎对象

#print('等会谁（哪个模块哪个抱）在使用我：',__name__)

from app import routes,models #从app包中导入模块routes





