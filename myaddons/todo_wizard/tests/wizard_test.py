#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Robert"
# Date: 2018/4/22  0022

from odoo.tests.common import TransactionCase


class TestWizard(TransactionCase):
    def setup(self, *args, **kwargs):
        super(TestWizard, self).setup(*args, **kwargs)

    # Add test setup code here...
    def test_populate_tasks(self):
        """populate tasks buttons should add two tasks"""
    # Add test code
