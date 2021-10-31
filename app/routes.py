from flask import render_template, flash,redirect

from app import app
from app.forms import LoginForm

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

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg='Login requested for user {},remember_me={}'.format(form.username.data,form.remember_me.data)
        flash(msg)

        return redirect("/index")
    login_form=LoginForm()
    return render_template('login.html',title='login',form=login_form)