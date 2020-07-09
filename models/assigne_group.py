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

class AssignGroup(models.Model):

    _name = 'info.assign.groups'
    _description = 'AssignementGroup'
    
    name = fields.Char(string="Assignement Group Name")
    info_group_id = fields.Many2one('info.res.users',string="Group", required=True)

    @api.constrains('info_group_id')
    def _onchange_groups(self):
        
        records = self.env['info.incidents.incidents'].search([('info_assignement_group_id', '=', self.id)])
        
        if not records:
            return
        
        for rec in records:

            if rec.filter_user_list:
                rec.write({'filter_user_list': [( 5, 0, 0)]})

            if self.info_group_id.user_list:
                if rec.info_assigned_to:
                    if rec.info_assigned_to not in self.info_group_id.user_list:
                        rec.info_assigned_to = False
                for user in self.info_group_id.user_list:
                    rec.write({'filter_user_list': [( 4, user.id)]})
            else:
                rec.info_assigned_to = False
            

            
                
                    
    