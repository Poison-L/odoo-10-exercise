# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")

    @api.one
    def do_toggle_done(self):
        # 责任人才可以执行状态切换
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()

    @api.multi
    def do_clear_done(self):
        # 波兰表达式
        domain = [('is_done', '=', True),
                  '|', ('user_id', '=', self.env.uid),
                  ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
