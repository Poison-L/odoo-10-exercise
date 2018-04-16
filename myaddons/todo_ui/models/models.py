# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('标签', size=40, translate=True)


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = u'To-do Stage'
    _order = 'sequence,name'

    # String fields:
    name = fields.Char(string='名称', size=40, translate=True)
    desc = fields.Text('描述')
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'),
         ('done', 'Closed')], '状态')
    docs = fields.Html('文件')

    # Numeric fields:
    sequence = fields.Integer('序列')
    perc_complete = fields.Float('% Complete', (3, 2))

    # Date fields:
    date_effective = fields.Date('有效日期')
    date_changed = fields.Datetime('最后修改时间')

    # Other fields:
    fold = fields.Boolean('folded?')
    image = fields.Binary('图片')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
