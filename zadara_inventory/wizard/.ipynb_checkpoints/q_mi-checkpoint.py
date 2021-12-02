# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime

from odoo.exceptions import ValidationError , UserError


class q_mi(models.TransientModel):
    _name = 'zadara_inventory.q_mi'
    _description = 'Stock Quantity History'
    
    
 
    by_product = fields.Boolean()


    location_to = fields.Many2one('zadara_inventory.locations')

        
    
    def qmi(self): 
        mi_t = self.env['zadara_inventory.master_inventory'].search([])

        all = mi_t#self.env['zadara_inventory.master_inventory'].search(['product_id', '=', "neverfind"])
        for x in all:

            all = all - x 
            #how do make empty object
            
        
        #all = self.env['zadara_inventory.master_inventory'].search([['location_id', '=', location_id.id]])
        #pro = self.env['zadara_inventory.product'].search([])
        #for x in pro: 
            
        
        
        
       
        loc_t = self.env['zadara_inventory.locations'].search([])
        pro = self.env['zadara_inventory.product'].search([])
        if self.by_product:
            for y in pro:
              
                if y.product_trackSerialNumber == True:
                    temp = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', y.id], ['location_id', '=', self.location_to.id]])
                    for x in temp:
                        x.report_q_mi = len(temp)
                    for i in temp:
                        all = all + i
                        break
                else:
                    temp = self.env['zadara_inventory.master_inventory'].search([['product_id', '=', y.id], ['location_id', '=', self.location_to.id]])
                    for x in temp:
                        x.report_q_mi = temp.quantity
                    for i in temp:
                        all = all + i
                        break

        
        
        
        
        
        
        
        

        
        '''
        #if self.by_location:
        h = self.env['zadara_inventory.master_inventory']
        for x in all:     
            if h.product_id.id == x.product_id.id and h.location_id.id == x.location_id.id and x.serial_number != 'N/A':
                if self.by_product:
                    all = all - x 
                else:
                    x.report_q_mi = h.report_q_mi
                    h = x 
                    
            else:    
                count = unt.return_tq_wl(x.product_id.id,x.location_id.id)
                x.report_q_mi = count
                h = x
        if self.by_product:
            temp2 = all 

            temp = all

            for x in temp2: 
                for y in all:  

                    if y.product_id.id == x.product_id.id and y.location_id.id == x.location_id.id:


                        if x.id != y.id and y.id > x.id:
                            all = all - y
        
        '''

        
        action = {
            'type': 'ir.actions.act_window',
            #'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree',
            'name': 'Products',
            'res_model': 'zadara_inventory.master_inventory',
            
            'domain': [['id','in',all.ids]],
        }
        return action
       
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    