#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Robert"
# Date: 2018/4/13 0013

from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):
    def test_create(self):
        """
        Create a simple Todo
        """
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
