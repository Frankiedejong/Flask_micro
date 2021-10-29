#从flask包里导入Flask类
from flask import Flask

app=Flask(__name__)

print('等会谁（哪个模块哪个抱）在使用我：',__name__)

from app import routes #从app包中导入模块routes





