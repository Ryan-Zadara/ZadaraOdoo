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
    
    @api.model
    def do_stuff(self):
        raise UserError(datetime.now())
    
   # def check_min(self, p_id,quant):
        
    #    t = self.env['zadara_inventory.min_inventory'].search([['product_id','=',p_id],['min_inv','>=',quant]])
     #   
      #  if t:
       #     if not self.env['zadara_inventory.low_inv_manager'].search([['product_id','=',p_id],['sent','=',False]]):
        #        vals_list = {'product_id': p_id, 'quantity': quant , 'sent':False, 'date_':datetime.now()}
         #       self.env['zadara_inventory.low_inv_manager'].create(vals_list)
                
        
    @api.model
    def create(self,vals_list):
        raise UserError(self.env['zadara_inventory.low_inv_manager'].id())
        res = super(low_inv_manager, self).create(vals_list)
        return res

    
    
    
    
    