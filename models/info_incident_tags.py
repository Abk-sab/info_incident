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

class IncidentTgas(models.Model):

    _name = 'info.incident.tags'
    _description = 'IncidentTga'
    
    name = fields.Char(string="Incident Tag")
    info_desc_tag = fields.Text(string="Description")
