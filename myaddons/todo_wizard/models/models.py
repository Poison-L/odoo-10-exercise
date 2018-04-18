# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo import exceptions

_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _description = '工作计划向导'

    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline = fields.Date('Deadline to Set')
    # res.users 是？？？
    new_user_id = fields.Many2one('res.users', string='Responsible to Set')

    @api.multi
    def do_mass_update(self):
        self.ensure_one()

        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update!')
        _logger.debug('Mass update on Todo Tasks %s',
                      self.task_ids.ids)
        vals = {}
        if self.new_deadline:
            vals['date_deadline'] = self.new_deadline
        if self.new_user_id:
            vals['user_id'] = self.new_user_id
        # Mass write values on all selected tasks
        if vals:
            self.task_ids.write(vals)
        return True
