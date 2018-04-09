# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class mymodule(models.Model):
#     _name = 'mymodule.mymodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Fruits(models.Model):
    _name = 'mymodule.fruits'   # 模块名_对象名

    name = fields.Char(string="水果名称", required=False, )
