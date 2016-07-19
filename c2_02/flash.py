#-*- encoding=UTF-8 -*-

from flask import Flask, render_template, request, redirect #导入模块

app = Flask(__name__)   #创建对象

@app.route('/') #指定根路径的回调
@app.route('/index/')
def index():
    return 'hello'

@app.route('/profile/<uid>/')
def profile(uid):
    #return 'profile : ' + uid
    colors = ('blue', 'red', 'green')
    return render_template('profile.html', uid=uid, colors=colors)

@app.route('/profileInt/<int:uid>/')
def profileInt(uid):
    return 'profileInt : ' + str(uid)

@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html', request=request.url)

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/redirct/<int:number>')
def redirctPage(number):
    return redirect('/newpath',code=number)


if __name__ == '__main__':
    app.run(debug=True) # debug,开启debug模式
