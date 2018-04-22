# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NewModule(models.Model):
    _inherit = 'todo.task'

    color = fields.Integer(string="色号", required=False, )
    priority = fields.Selection([('0', 'Low'), ('1', 'Normal'), ('2', 'High')], string="优先级", default='1')
    kanban_state = fields.Selection([('normal', 'In Progress'), ('blocked', 'Blocked'), ('done', 'Ready for next stage')],
                                    string="看板状态", default='normal')
