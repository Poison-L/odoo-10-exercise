# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Blog(models.Model):
    _name = 'my.blog'
    _description = u'论坛'

    name = fields.Char(string="名称", required=False, )


# class Fruits(models.Model):
#     _name = 'my.fruits'   # 模块名_对象名
#
#     name = fields.Char(string="水果名称", required=False, )
