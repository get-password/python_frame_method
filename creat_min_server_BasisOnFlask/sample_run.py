from flask import Flask, render_template, jsonify
from lagou_spider.handle_insert_data import lagou_mysql

# 实例化flask
app = Flask(__name__)

# 注册路由
@app.route("/", methods=["GRT"])
def index():
    return "Hello World"


if __name__ == '__main__':
    # 启动flask
    app.run(debug = True,host="0.0.0.0",port=80)