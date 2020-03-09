# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class low_inv_manager(models.Model):
    _name = 'zadara_inventory.low_inv_manager'
    _description = 'locations'

    product_id = fields.Many2one('zadara_inventory.product')
    
    quantity = fields.Integer()
    
    sent = fields.Boolean(default=False)
    
    date_ = fields.Datetime(Default = datetime.now())
    
    
    
    def check_min(self, p_id,quant):
        t = self.env['zadara_inventory.min_inventory'].search([['product_id','=',self.p_id],['min_inv','>=',quant]])
        
        
        
    
    
    
    
    
    