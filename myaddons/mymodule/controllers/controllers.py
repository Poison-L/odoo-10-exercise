# -*- coding: utf-8 -*-
from odoo import http


class MyBlog(http.Controller):
    @http.route('/blog/', auth='public')
    def index(self, **kw):
        return "1313131313131"

# class Mymodule(http.Controller):
#     @http.route('/my/fruits/', auth='public', website=True)
#     def index(self, **kw):
#         # return "Hello, world"
#
#         fruits = http.request.env['my.fruits']
#
#         return http.request.render('mymodule.index',
#                                    {'fruits': fruits.search([])})


