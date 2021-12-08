# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# 'sale','base','web_map','stock','purchase'
{
    'name': 'X Development',
    'version': '1.0',
    'category': 'Hidden/Tools',
    'author': "Ivan Suhendra",
    'website': "https://www.loremibsum.com",
    'summary': 'Documentation',
    'description': """
This module gives a framework for my sample
----------------------------------------------------

# 'depends': ['sale','base','web_map','stock','purchase']
The service is provided by the In App Purchase Odoo platform.
""",
    'depends': ['sale','base_setup'],
    'data': [
        'security/ir.model.access.csv',

        'views/menu_views.xml',
        'views/customer_view.xml',
        'views/car_view.xml',
        'views/order_view.xml',
        'views/main_development_view.xml',
        'views/pembagian_hasil_view.xml',

        'wizard/app_sp_tunggakan_wizard.xml',
        'wizard/app_pembagian_hasil_penjualan_wizard_view.xml',

        'report/qm_auto_packing_report.xml',
        'report/odes_coa_check_report.xml',
        'report/app_journal_print_report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
