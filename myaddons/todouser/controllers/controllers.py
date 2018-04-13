# -*- coding: utf-8 -*-
from odoo import http

# class Todouser(http.Controller):
#     @http.route('/todouser/todouser/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todouser/todouser/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todouser.listing', {
#             'root': '/todouser/todouser',
#             'objects': http.request.env['todouser.todouser'].search([]),
#         })

#     @http.route('/todouser/todouser/objects/<model("todouser.todouser"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todouser.object', {
#             'object': obj
#         })