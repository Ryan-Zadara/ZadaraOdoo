# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_a_customer = fields.Boolean(string='Is Customer?')
    is_a_vendor = fields.Boolean(string='Is Vendor?')

