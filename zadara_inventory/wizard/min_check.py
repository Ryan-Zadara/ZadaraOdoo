# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime

from odoo.exceptions import ValidationError , UserError


class min_check(models.TransientModel):
    _name = 'zadara_inventory.min_check'
    _description = 'Stock Quantity History'
    
    nextcall = fields.Datetime()
    
    
    
    