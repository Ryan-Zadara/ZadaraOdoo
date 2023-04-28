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

    def create(self, vals):
        res = super(StockMoveLine, self).create(vals)
        for rec in res.filtered(lambda l: l.picking_id):
            rec.partner_id = res.picking_id.partner_id or False
        return res
