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

class IncidentCloseCode(models.Model):

    _name = 'info.incident.close.code'
    _description = 'IncidentCloseCode'
    
    name = fields.Char(string="Incident Close Code")
    info_desc_close_code = fields.Text(string="Description")


