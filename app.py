from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/user/<int:id>')
def show_user_profile(id):
    return 'User %d' % id

@app.route('/post/<float:id>')
def show_post(id):
    return 'Post %d' % id

'''
if __name__ == '__main__':
    app.run()
    app.run(debug=True)
    app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, threaded=True)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, threaded=True, processes=5)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, threaded=True, processes=5, passthrough_errors=True)
'''






# func1：没有flask命令的旧版Flask，通过下述方式启动启动应用
if __name__ == '__main__':
    app.run()
    app.run(debug=True)

'''
#func2：已经拥有新版flask run 命令，无需使用上述方式，不过仍旧有效
#启动虚拟环境
(base) yangjinchuandeMacBook-Air:flasky yjc$ source venv/bin/activate
#执行得到app运行
(venv) (base) yangjinchuandeMacBook-Air:flasky yjc$ export FLASK_APP=app.py
#debug加入pin码防篡改
(venv) (base) yangjinchuandeMacBook-Air:flasky yjc$ export FLASK_DEBUG=1
# 执行flask应用
(venv) (base) yangjinchuandeMacBook-Air:flasky yjc$ flask run

'''
