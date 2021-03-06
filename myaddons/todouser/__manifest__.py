# -*- coding: utf-8 -*-
{
    'name': "Multiuser To-Do",

    'summary': """
        将任务应用扩展到多用户""",

    'description': """
        Extend the To-Do app to multiuser.
    """,

    'author': "Robert",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todotask', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
        # 'data/todo.task.csv',
    ],
    'application': True,
}
