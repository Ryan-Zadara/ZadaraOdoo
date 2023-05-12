
# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    part_number_ids = fields.One2many('product.number', 'product_id', string="Part Number")
    # vendor_id = fields.Many2one('res.partner', string="Vendor")
    sub_categ_id = fields.Many2one('product.subcategory', string='Sub Category')


class ProductNumber(models.Model):
    _name = 'product.number'
    _description = 'Product Number'

    name = fields.Char('Product Number')
    product_id = fields.Many2one('product.template', string="Product Name")


class ProductSubcategory(models.Model):
    _name = 'product.subcategory'
    _description = 'Product Subcategory'

    name = fields.Char(string= 'Name')
