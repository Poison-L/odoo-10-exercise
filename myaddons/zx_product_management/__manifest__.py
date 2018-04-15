# -*- coding: utf-8 -*-
{
    'name': "ZX Product Management",

    'summary': """
        产品管理系统""",

    'description': """
        产品管理系统，提供产品管理功能。
    """,

    'author': "Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/workflow.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 应用中默认能搜索到请假单模块
    'application': True,
}
