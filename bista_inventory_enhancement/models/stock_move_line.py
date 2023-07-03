# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    partner_id = fields.Many2one('res.partner', string='Contact')
    product_tag_id = fields.Many2one('product.tag', string='Product Tag')

    def create(self, vals):
        res = super(StockMoveLine, self).create(vals)
        for rec in res.filtered(lambda l: l.picking_id):
            rec.partner_id = res.picking_id.partner_id or False
        return res


class ProductTag(models.Model):
    _name = 'product.tag'
    _description = 'Product Tag'

    name = fields.Char(string='Name')
