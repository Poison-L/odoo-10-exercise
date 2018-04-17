# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    # 计算字段
    stage_fold = fields.Boolean('Stage Folded?',
                                compute='_compute_stage_fold',
                                # store=False, # the default
                                search='_search_stage_fold',
                                inverse='_write_stage_fold'
                                )

    # 关联字段
    stage_state = fields.Selection(string='Stage State', related='stage_id.state')

    # 计算字段方法
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    # SQL约束 不让活动任务具有相同标题
    _sql_constraints = [('todo_task_name_uniq',
                         'UNIQUE (name, active)',
                         'Task title must be unique!')]

    # python约束 名称至少5个字符
    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Must have 5 chars!')

