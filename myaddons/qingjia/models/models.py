# -*- coding: utf-8 -*-

from odoo import models, fields, api


class qingjiadan(models.Model):
    """
    Request for absence
    """

    WORKFLOW_STATE_SELECTIOBN = [
        ('draft', '草稿'),
        ('confirm', '待审批'),
        ('complete', '已完成')
    ]

    _name = 'qingjia.qingjiadan'    # 模块名_对象名

    name = fields.Char(string="申请人")
    days = fields.Integer(string="天数")
    startdate = fields.Date(string="开始日期")
    reason = fields.Text(string="请假事由")
    state = fields.Selection(WORKFLOW_STATE_SELECTIOBN,
                             default='draft',
                             string='状态',
                             readonly=True)     # 只读，不可修改

    @api.multi
    def do_confirm(self):
        self.state = 'confirm'
        return True

    @api.multi
    def do_complete(self):
        self.state = 'complete'
        return True

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
