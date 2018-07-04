# -*- coding: utf-8 -*-
import os
import sys
from odoo import http, models, SUPERUSER_ID
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import FileSystemLoader


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
# 加载文件
templateLoader = FileSystemLoader(searchpath=BASE_DIR + "/templates")
env = Environment(loader=templateLoader, autoescape=True)


class Test(http.Controller):

    @http.route()
    def foo(self, **kwargs):
        pass
        datalist = []
        template = env.get_template("index.html")
        # 加载一个模板: template = env.get_template(‘mytemplate.txt’), 使用env的模板环境加载名为#mytemplate.txt的模板文件.
        return template.render(data=datalist)  # datalist是待传入数据，比如列表
    # 渲染一个模板: template.render(name = ‘Jack’), 渲染模板template, 传入了模板参数name值为Jack

# class Qingjia(http.Controller):
#     @http.route('/qingjia/qingjia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qingjia/qingjia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qingjia.listing', {
#             'root': '/qingjia/qingjia',
#             'objects': http.request.env['qingjia.qingjia'].search([]),
#         })

#     @http.route('/qingjia/qingjia/objects/<model("qingjia.qingjia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qingjia.object', {
#             'object': obj
#         })
