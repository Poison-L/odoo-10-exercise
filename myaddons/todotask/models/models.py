# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = u'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?', )
    active = fields.Boolean('Active?', default=True)
    stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold')

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    @api.model
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True

    # 练习计算字段
    # @api.depends('stage_id.fold')
    # def _compute_stage_fold(self):
    #     for task in self:
    #         task.stage_fold = task.stage_id.fold
