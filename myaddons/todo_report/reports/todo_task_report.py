#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Robert"
# Date: 2018/5/1  0001

from odoo import models, fields


class TodoReport(models.Model):
    _name = 'todo.task.report'
    _description = 'To-do Report'
    _sql = """
            CREATE OR REPLACE VIEW todo_task_report AS
            SELECT *
            FROM todo_task
            WHERE active = True
            """
    name = fields.Char('Description')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?')
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
