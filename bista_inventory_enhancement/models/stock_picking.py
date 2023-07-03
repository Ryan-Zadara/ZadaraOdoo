# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_no = fields.Char(string='Invoice Number')
    po_number = fields.Char(string='PO Number')
    funding_company_id = fields.Many2one('res.partner', string='Funding Company')
