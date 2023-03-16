from datetime import datetime
from flask import render_template, request
from run import app

@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')



@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """

    return {'name':1213}
