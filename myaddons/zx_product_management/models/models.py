# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductManagement(models.Model):
    """
    Request for absence
    """

    WORKFLOW_STATE_SELECTIOBN = [
        ('draft', '草稿'),
        ('confirm', '待审批'),
        ('complete', '已完成')
    ]

    _name = 'product.management'

    name = fields.Char(string="产品名称", required=True)
    price = fields.Float(string="产品价格",  required=True)
    number = fields.Integer(string="产品数量", required=True)
    startdate = fields.Date(string="提交日期", required=True)
    note = fields.Text(string="备注", default=None)
    state = fields.Selection(WORKFLOW_STATE_SELECTIOBN, default='draft', string='状态',
                             readonly=True)  # 只读，不可修改

    @api.multi
    def do_confirm(self):
        self.state = 'confirm'
        return True

    @api.multi
    def do_complete(self):
        self.state = 'complete'
        return True
