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

class IncidentUrgency(models.Model):

    _name = 'info.incident.urgency'
    _description = 'IncidentUrgency'
    
    name = fields.Char(string="Name",compute="get_concatenate_values", store=True, readonly=True)
    info_name = fields.Char(string="Urgency")
    info_value = fields.Integer(string="Urgency Value")


    @api.multi
    @api.depends('info_name','info_value')
    def get_concatenate_values(self):
        for r in self:
            if(r.info_value and r.info_name):
                result = "%d - %s" % \
                         (r.info_value or '', r.info_name or 0.0)
                self.name=result 

