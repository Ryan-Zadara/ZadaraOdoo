# -*- coding: utf-8 -*-

from odoo import fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class inv_repo_two(models.TransientModel):
    _name = 'zadara_inventory.inv_repo_two'
    _description = 'Stock Quantity History'
    
    inv_at_date = fields.Datetime(default=lambda self: fields.datetime.now())
    
    by_product = fields.Boolean()
   
    #by_location = fields.Boolean()
    
    add_serial_number = fields.Boolean()
        
    
    def calc_at_date(self):
        #if self.locations == None:
            #location_id = self.env['zadara_inventory.product_history'].get.context('product_history')
        self.env['zadara_inventory.m_inv_copy'].reset_copy()
     #   products = self.env['zadara_inventory.product'].search([])
        all = self.env['zadara_inventory.m_inv_copy']
       # for_search  = self.env['zadara_inventory.product_history'].search([])
        mi_t = self.env['zadara_inventory.master_inventory'].search([])
        #mi_ph =  self.env['zadara_inventory.product_history'].search([])
      #  temp = self.env['zadara_inventory.product_history']#.search((['date_','<=', self.inv_at_date]), order='date_desc')
        qu_t = self.env['zadara_inventory.update_quantity']
        t_t = self.env['zadara_inventory.transfer']
        r = 0
        
        for x in mi_t:
            
            
            
            updates = self.env['zadara_inventory.transfer'].search((['transfer_date','<=', self.inv_at_date],['product_id.id','=',x.product_id.id],['serial_number','=',x.serial_number]),order="transfer_date desc", limit=1)
            if not updates:
                updates = self.env['zadara_inventory.update_quantity'].search((['update_date','<=', self.inv_at_date],['product_id.id','=',x.product_id.id],['serial_number','=',x.serial_number]),order="update_date desc", limit=1)
            if updates:
                self.product_id = x.product_id.id
                self.serial_number = x.serial_number
                self.quantity = x.quantity
                self.report_q_mi = updates.t_quantity
                self.location_id = updates.location_id.id
                self.product_number = x.product_number.id
                #raise UserError(updates)
                if not updates.p_tag == None:
                    self.p_tag = updates.p_tag.id
                    r = r + 1
                    #all = all | temp
                else:
                    self.p_tag = x.p_tag.id
                dic = [{'product_id':self.product_id,'p_tag':self.p_tag,'location_id':self. location_id,'serial_number':self.serial_number,'quantity':self.quantity,'product_number':self.product_number,'report_q_mi':self.report_q_mi}]
                self.env['zadara_inventory.m_inv_copy'].create(dic)
              #  l = self.env['zadara_inventory.m_inv_copy'].search([])
              #  raise UserError(l)
        for x in self.env['zadara_inventory.m_inv_copy'].search([]):
          #  raise UserError(x)
            all = all | x
                  #  raise UserError(all)
       # raise UserError(r)
        #raise UserError(all)
    
        #test_ = self.env['zadara_inventory.product_history'].search(['date_','<=', self.inv_at_date])
       
        #for x in mi_ph:
         #   if x.if_date(x.date_,self.inv_at_date):
         #       temp = temp | x
        #for x in temp:
        #    temp2 = temp.search((['product_id.id','=',x.product_id.id],['serial_number','=',x.serial_number],['location_id.id','=',x.location_id.id]))
         #   l = x
          #  for t in temp2: 
           #     if t.date_ > x.date_:
           #         l = t
           # all = all | l
           # temp = temp - temp2
            #updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['product_id.id','=',x.product_id.id],['location_id.id','=',x.location_id.id],['serial_number','=',x.serial_number]),order="date_ desc")
                
        #raise UserError(all)        
                 
            #temp = temp | updates
                
       # for x in all: 
            
            
        
           #raise UserError(all)
        
        
        
       # elif not self.by_location:
       #     for x in mi_t:
       #         updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.product_id.id],['mi_id.serial_number','=',x.serial_number],['location_id','=',x.location_id.id]),order="date_ asc", limit=1)
                #updates = self.env['zadara_inventory.product_history'].search((['date_','<=', self.inv_at_date],['mi_id.product_id','=',x.id],['location_id','=',self.location_id.id]),order="date_ asc", limit=1)
                
        #        all = updates | all 
        
        
        
        
        
   #     z = all.search([],order="product_id asc")
   #     unt = all
     #   h = self.env['zadara_inventory.master_inventory']
    #    for x in z:     
           # raise UserError(x.product_id.id)
        #    if h.product_id.id == x.product_id.id and h.location_id.id == x.location_id.id and x.serial_number != 'N/A':
         #       if self.by_product:
                    #raise UserError(x)
           #         all = all - x 
          #      else:
           #   #      x.report_q_mi = h.report_q_mi
          #          h = x 
                    
           # else:    
                #count = unt.return_tq_wl(x.product_id.id,x.location_id.id)
            
                #raise UserError(count)
            
                #x.report_q_mi = count
               # h = x        
                
                

       
       
        #if self.by_location:
        #for x in all:     
            
        #    count = unt.ph_return_tq_wl(x.product_id.id,x.location_id.id)
            #raise UserError(count)
            
         #   x.t_quantity = count
        #else:
        #    for x in all: 
        #        count = unt.ph_return_tq(x.product_id.id)
                #raise UserError(count)
            
        #        x.t_quantity = count
        #raise UserError(all.search['id','=',1])

       # if not self.add_serial_number:
       #     cop = self.env['zadara_inventory.product_history'].browse([])
       #     for x in all:
               
       #         cop = cop | all.search((['product_id.id','=',x.product_id.id],['location_id.id','=',x.location_id.id]), limit=1)
       #     all = cop
        
        if self.by_product:
            #temp3 = self.env['zadara_inventory.product_history']
            temp2 = all #self.env['zadara_inventory.product_history'].search(['ids','in',all.ids])
            #self.env['zadara_inventory.product_history'].browse(all)
            #temp2 = 
            temp = all
          
            for x in temp2: 
                for y in all:  
                 
                    if y.product_id.id == x.product_id.id and y.location_id.id == x.location_id.id:
                        
                        
                        if x.id != y.id and y.id > x.id:
                           all = all - y
               
  
            
            
        
        action = {
            'type': 'ir.actions.act_window',
            #'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree',
            'name': 'Products',
            'res_model': 'zadara_inventory.m_inv_copy',

            'domain': [['id','in',all.ids]],
        }



        return action
       
        
       # master = updates.get.context()
        
        #for x in updates and y in transfers:
        #    product = x.context.get('product_id')
            
        
    
    