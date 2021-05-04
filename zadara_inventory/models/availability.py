# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class availability(models.Model):
    _name = 'zadara_inventory.availability'
    _description = 'zadara_inventory.availability'
    
    #product_id = fields.Many2one('zadara_inventory.product')
    
    #name = fields.Char()
    
    #short_name = fields.Char(help='Nickname')
    
    #location_id = fields.Many2one('zadara_inventory.locations')
    
    serial_number = fields.Char(string="Serial Number", required = True)
    
    availability_Type = fields.Selection([('Available','Available'), ('Unavailable','Unavailable')], required=False)
    
    p_tag = fields.Many2one('zadara_inventory.p_tag', required = False)
    
    available_date = fields.Datetime(default=lambda self: fields.datetime.now())

    
    
    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            mi = self.env['zadara_inventory.master_inventory'].search([['serial_number', '=', val.get('serial_number')]])
            if not mi:
                raise UserError("Serial Number Not Found") 
            #if not self.env['zadara_inventory.p_tag'].search([['name','=',val.get('p_tag')]]) and val.get('p_tag') != None:
            #    raise UserError("P_Tag Not Found")
            
            if val.get('availability_Type') == False: 
                 val['availability_Type'] = mi.availability_Type

            if val.get('p_tag') == False:
                val['p_tag'] = mi.p_tag.id
            mi.p_tag = val.get('p_tag')
            mi.availability_Type = val.get('availability_Type')

        res = super(availability, self).create(vals_list)
        return res
    
        
        
        
        
        
        
        
        
        
