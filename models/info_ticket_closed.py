# -*- coding: utf-8 -*-
###################################################################################
# Create info.res.users to select Roles
# the concept in this model is quite similar to base.user.role module
# 
#
###################################################################################

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__) 

class ClosedTicketConfiguration(models.Model):

    _name = 'info.closed.ticket'
    _description = 'ClosedTicket'
    
    name = fields.Char()
    days_to_closed = fields.Integer(default="3")
