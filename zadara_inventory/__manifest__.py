# -*- coding: utf-8 -*-
{
    'name': "Zadara Inventory",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
       
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/master_inventory_view.xml',
         'views/mi_mass_update.xml',
        'views/min_inventory.xml',
        'views/views.xml',
        'views/low_inv_manager.xml',
        'views/m_inv_copy.xml',
        #'data/lim_trigger.xml',
         'views/p_tag.xml',
        'views/location.xml',
        'views/master_inventory.xml',
        'views/moves.xml',
        'views/product.xml',
        'views/product.xml',
        'views/product_history.xml',
        'views/product_number.xml',
        'views/vendors.xml',
        'wizard/inv_report_calc.xml',
         'wizard/inv_repo_two.xml',
        'wizard/q_mi.xml',
        'views/update_quantity.xml',
        'views/transfer.xml',
        'views/availability.xml',
        'views/menus.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
