from flask import render_template

from app import app

#2个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
    user={'username':'qiya'}
    #创造一个列表：帖子，里面的元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容
    posts=[
        {
            'author':{'username':'John'},
            'body' :'Beautiful day in Porland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='home',user=user,posts=posts)