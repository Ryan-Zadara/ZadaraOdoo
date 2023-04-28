# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Bista Inventory Enhancement',
    'version': '1.0',
    'sequence': 7,
    'category': 'Stock',
    'summary': "This Module Allows is for Inventory Enhancements.",
    'description': """
            This Module has following Features
            1. Part Number in the product
    """,
    'website': 'https://www.bistasolutions.com',
    'author': 'Bista Solutions',
    'images': [],
    'depends': ['stock', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/product_number_views.xml'
    ],
    'application': True,
    'installable': True,
}
