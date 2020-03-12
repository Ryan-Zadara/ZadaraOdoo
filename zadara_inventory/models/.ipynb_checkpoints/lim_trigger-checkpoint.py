# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class lim_trigger(models.Model):
    _name = 'zadara_inventory.lim_trigger'
    _description = 'locations'
    
    
   # @api.model
    def do_stuff(self):
        raise UserError("workse")