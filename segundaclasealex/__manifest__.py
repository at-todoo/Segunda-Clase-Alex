# -*- coding: utf-8 -*-
{
    'name': "segundaclasealex",

    'summary': """
        Segunda Clase Ales""",

    'description': """
        Ahora si se pudo
    """,

    'author': "Todoo SAS",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Rock',
    'version': 'Metal',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
