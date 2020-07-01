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

class ResUserRoles(models.Model):

    _name = 'info.res.users'

    name = fields.Char(string="Name")
    group_id = fields.Many2one('res.groups')
    user_list = fields.One2many('res.users', 'knowledge_res_id', string="User List")

    @api.constrains('group_id','user_list')
    def _change_user_knowledge_group(self):

        """Delete users from groups"""

        for user_id in self.group_id.users.ids:
            if user_id not in self.user_list.ids:
                rec = self.env['res.users'].search([('id', '=', user_id)])
                rec.write({'groups_id': [( 3, self.group_id)]})

        for user_id in self.user_list.ids:
            if user_id not in self.group_id.users.ids:
                rec = self.env['res.users'].search([('id', '=', user_id)])
                rec.write({'groups_id': [( 4, self.group_id)]})

        _logger.warning('groups')
        _logger.warning(self.group_id.users)
        _logger.warning('user_list')
        _logger.warning(self.user_list)
