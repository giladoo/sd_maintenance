# -*- coding: utf-8 -*-
{
    'name': "SD Maintenance",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://giladoo.com/sd_maintetance",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '18.0.1.0.0',


    # any module necessary for this one to work correctly
    'depends': ['base', 'web','hr', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_equipments_views.xml',

    ],
    'assets': {
        # 'website.assets_editor': [
        #     'static/src/**/*',
        # ],
        'web.assets_qweb': [
            ],
        'web.assets_frontend': [

        ],
        'web.assets_backend': [

        ],
    },

    # only loaded in demonstration mode
    'license': 'LGPL-3',

}
