# -*- coding: utf-8 -*-
{
    'name': "Purchase Request Extension",

    'summary': """
        Esta modulo tiene como objetivo agregar funcionalidad a los purchase request """,

    'description': """
        Aca podria escribir mucho mas para hacer una descripcion mas completa del modulo
    """,

    'author': "Agustin Pighin",
    'website': "http://www.droguerialatrinidad.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'depends': [
        'hr',
        'purchase_request'
    ],
    'category': 'test',
    'version': '9.0.0.0.6',
    'installable': False,
    'auto_install': False,
    'application': False

    # any module necessary for this one to work correctly
    

    # always loaded
     #'data': [
        # 'security/ir.model.access.csv',
        #'views/openacademy.xml',
        #'views/partner.xml',
     #],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}