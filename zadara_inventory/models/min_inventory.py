# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class min_inventory(models.Model):
    _name = 'zadara_inventory.min_inventory'
    _description = 'locations'
    
    product_id = fields.Many2one('zadara_inventory.product')
    
    min_inv = fields.Integer()
    
    
    
    
    
    
    
    
    
