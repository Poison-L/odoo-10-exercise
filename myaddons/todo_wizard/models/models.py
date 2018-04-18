# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _description = '工作计划向导'

    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline = fields.Date('Deadline to Set')
    # res.users 是？？？
    new_user_id = fields.Many2one('res.users', string='Responsible to Set')
