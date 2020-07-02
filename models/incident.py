# -*- coding: utf-8 -*-
###################################################################################
#
#    Incident Model and functions
#
###################################################################################

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__) 


class InfoIncident(models.Model):
    _name = 'info.incidents.incidents'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    

    """Fileds Declaration
       ------------------
       Number: Character
       Caller : M2o 
       Category: Selection
       Subcategory: Selection
       Contact Type: Selection
       State: Selection
       Impact: Selection
       Urgency: Selection
       Priority: Selection
       Assignement group: M2o
       Assigned to: M2o
       Short description: Character
       Skills: O2m
       On Hold Reason: Selection       
        """
    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Number", readonly=True, required=True, copy=False, default='New')
    
    info_caller = fields.Many2one('res.partner',string="Caller", required=True)


    info_subca_ids = fields.One2many('info.incidents.subcategory', inverse_name='info_subcat_incident_id', string="Subcategory")

    info_subca_id = fields.Many2one('info.incidents.category', string="Category")


    info_contact_type = fields.Char(string="Contact Type")
    info_state = fields.Selection([('new', 'New'),
                                   ('inprogress', 'In progress'),
                                   ('onhold', 'On Hold'),
                                   ('resolved','Resolved'),
                                   ('closed', 'Closed'),
                                   ('cancelled', 'Cancelled')], default='new',group_expand='_expand_states', index=True)

    info_impact = fields.Selection([('1', 'High'),
                                    ('2', 'Medium'),
                                   ('3', 'Low')],string="Impact")

    info_urgency = fields.Selection([('1', 'High'),
                                   ('2', 'Medium'),
                                   ('3', 'Low')],string="Urgency")

    info_priority = fields.Selection([('1', 'Critical'),
                                   ('2', 'High'),
                                   ('3', 'Moderate'),
                                   ('4','Low'),
                                   ('5', 'Planning')],string="Priority")

    info_assignement_group_id = fields.Many2one('info.assign.groups',string="Assignment group", required=True)
    info_assigned_to = fields.Many2one('res.users',string="Assigned to", required=True)

    info_short_desc = fields.Char(string="Short description")
    info_desc = fields.Text(string="Description")

    # info_skills_id = fields.One2many('info.incidents.skills', 'skills_id', string="Skills")

    info_reason = fields.Selection([('caller', 'Awaiting Caller'),
                                     ('change', 'Awaiting Change'),
                                     ('problem', 'Awaiting Problem'),
                                     ('vendor','Awaiting Vendor')],string="Reason on Hold")      

    info_Knowledge = fields.Many2one('info.knowledge.knowledge', string="knowledge")

    # info_res_code = fields.Many2many('info.knowledge.tag', 'knowlede_article_tas_rel', 
    #                         'article_id', 'tag_id', string="Tags")

    info_res_notes = fields.Text(string="Resolution notes")
    info_res_by = fields.Many2one('hr.employee',string="Resolved by")
    info_res_date = fields.Date(string="Resolved date")
   
    @api.model
    def create(self, vals):
       if vals.get('name', 'New') == 'New':
           vals['name'] = self.env['ir.sequence'].next_by_code('info.incidents.incidents') or 'New'

       result = super(InfoIncident, self).create(vals)
       return result

    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).info_state.selection]

    # def _get_default_info_state_id(self):
    #     """ Gives default stage_id """
    #     incident_id = self.env.context.get('default_incident_id')
    #     if not incident_id:
    #         return False
    #     return self.stage_find(incident_id, [('fold', '=', False)])




    # def stage_find(self, section_id, domain=[], order='sequence'):
    #     """ Override of the base.stage method
    #         Parameter of the stage search taken from the lead:
    #         - section_id: if set, stages must belong to this section or
    #           be a default stage; if not set, stages must be default
    #           stages
    #     """
    #     # collect all section_ids
    #     section_ids = []
    #     if section_id:
    #         section_ids.append(section_id)
    #     section_ids.extend(self.mapped('project_id').ids)
    #     search_domain = []
    #     if section_ids:
    #         search_domain = [('|')] * (len(section_ids) - 1)
    #         for section_id in section_ids:
    #             search_domain.append(('project_ids', '=', section_id))
    #     search_domain += list(domain)
    #     # perform search, return the first found
    #     return self.env['project.task.type'].search(search_domain, order=order, limit=1).id