# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = u'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?', )
    active = fields.Boolean('Active?', default=True)

    state = fields.Selection([('draft', 'New'),
                              ('open', 'Started'),
                              ('done', 'Closed')], '状态')

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
