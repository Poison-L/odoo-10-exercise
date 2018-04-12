# -*- coding: utf-8 -*-
{
    'name': "todo task app",

    'summary': """
        工作计划管理系统""",

    'description': """
        工作计划管理系统：安排你的工作计划。
    """,

    'author': "Robert",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
