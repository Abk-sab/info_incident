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

class IncidentImpact(models.Model):

    _name = 'info.incident.impact'
    _description = 'IncidentImpact'
    
    name = fields.Char(string="Impact")
    info_value = fields.Text(string="Impact Value")
