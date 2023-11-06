from flask import Flask,render_template

from flask import jsonify   #序列化

#app = Flask(__name__)

"""
传模板文件的时候，必须要再templates这个文件夹下面建立模板文件，如果想要更改路径
那么初始化就要改成app = Flask(__name__, template_folder='你的文件夹路径')
"""
add = Flask(__name__)

"""
路由，这里也叫路径的意思
    前端访问的时候会匹配到括号里面的路径，匹配成功就会进入到下面的视图函数
    ，因为是http协议,http是必须要有响应的，如下响应的就是一个字符串，必须要有一个返回值
    如果没有返回值的化就会报错的

"""
@add.route('/tianzi')   #路由绑定视图函数
def hello_world():  # put application's code here
    return 'Hello World!'


"""
注意路由里面的东西前面一定要加上一个 / 如果不加的话会报错的
"""
@add.route('/sss')
def sss():  # put application's code here
    """
    响应
    :return: 返回给前端的，我们这里叫做响应    这里返回的是字符串
    """
    return 'Hello World!1111'



"""
返回带标签
"""
@add.route("/t")
def t():
    """

    :return: 返回字符串,支持HTML标签
    """
    return "<b>hello world</b>"



"""
模板渲染
    必须要有templates这个路径的文件夹，返回的前端的代码的路径必须再templates文件夹里面
"""
@add.route("/index")
def index():
    """

    :return: render_template    用于模板渲染  后面的括号写前端的文件名
    文件名的后面还可以给文件传入数据,比如说我们再里面传入一个name=法外狂徒张三
    模板里面必须要有这个name

    这里面的模板渲染是指的是,先去加载这个html页面，加载完成之后,再去把这个name传过去,传递
    这个name的过程就叫模板渲染
    """
    return render_template("inddex.html",name="法外狂徒张三")




#如果返回的是json数据的话,也是可以返回的
"""
json    他有序列化和解析
            解析:呢是将我们的字符串变成json对象
            序列化:则是反过来，将我们的对象变成字符串
            再python中的json就是一个字典

"""











































































































































































@add.route("/json数据")
def json_shuju():
    #正常返回
    #return {"name":"张三","age":33}   #这个字典,他是一个对象python的对象
    #这个时候我们需要把他们变换成为字符串
    """
    :return: 通过jsonify这个函数可以将json对象转换成字符串
    """
    return jsonify({"name":"张三","age":33})




if __name__ == '__main__':
    """
    启动服务器run(),启动的时候还可以加参数
        debug = True
        debug 是否开启调试模式，开启后修改python代码会自动重启
            也就是可以让报错更加详细
            注意:这个只能再开发的时候写，上线的时候就不要写的，不然容易被黑
        post    启动指定的端口号，默认是5000，可以更改
        列如
            post = 5001         注意更改的时候一般都是4位
        host    主机，默认是127.0.0.1     这个是只能自己的局域网才能访问到自己
        指定为0.0.0.0代表本机所有ip  也就是同局域网下的所有机器都可以访问

    """
    add.run(debug=True,port=5001,host="0.0.0.0")

















"""
运行结果拆息
#这个是运行的一个路径
P:\测试代码\venv\Scripts\python.exe P:\测试代码\pythonWEB\FLASK框架\入门\FLASK入门简介.py 

#app后面的这个是告诉你运行的文件
 * Serving Flask app 'FLASK入门简介'



 #Debug 模式是 off
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.


#这个是我们的服务器地址
 * Running on http://127.0.0.1:5000

#CTRL+C退出的意思
Press CTRL+C to quit
127.0.0.1 - - [18/Oct/2023 20:29:23] "GET /sss HTTP/1.1" 200 -
127.0.0.1 - - [18/Oct/2023 20:30:12] "GET /sss HTTP/1.1" 200 -
127.0.0.1 - - [18/Oct/2023 20:30:12] "GET /favicon.ico HTTP/1.1" 404 -

进程已结束,退出代码0

"""



