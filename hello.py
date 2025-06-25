from datetime import datetime

from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 自定义错误页面
'''
在 Flask 中，@app.errorhandler(404) 定义的错误处理页面是自动触发的，当用户访问不存在的路由时，Flask 会自动调用这个函数并返回 404.html 页面。你不需要（也不应该）用 url_for() 手动生成它的 URL。
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 主动返回404页面
@app.route('/user/<name>')
def show_error(name):
    if not user:
        abort(404)
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
