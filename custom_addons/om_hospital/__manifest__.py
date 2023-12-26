# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Noman',
    'sequence': -100,  # view sequence of new addon
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'application': True,  # Shows in app
    'installable': True,
    'auto_install': False,
    'assets': {},
}
