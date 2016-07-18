#-*- encoding=UTF-8 -*-

from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key = 'aa'

@app.route('/')
@app.route('/index/')
def index():
    res = ''
    for msg in get_flashed_messages():
        res = res + msg + "<br>"
    return  res

@app.route('/profile/<int:uid>/', methods=['GET', 'POST'])
def profile(uid):
    #return 'profile:' + str(uid)

    colors = ('red', 'green', 'blue')
    infos = {'nowcoder':'abc', 'google':'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)

@app.route('/request')
def request_demo():
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '+++++' + request.path + '<br>'
    for property in dir(request):
        res = res + str(eval('request.'+property))+'\<br\>'
    return res

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url=request.url)

@app.route('/login')
def login():
    flash('登陆成功')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
