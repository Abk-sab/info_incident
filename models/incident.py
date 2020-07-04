# -*- coding: utf-8 -*-
###################################################################################
#
#    Incident Model and functions
#
###################################################################################

from odoo import models, fields, api, _
import logging
from datetime import datetime
from datetime import timedelta
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
    # info_state_re= fields.Selection(compute="state_rel")

    info_contact_type = fields.Char(string="Contact Type")
    info_state = fields.Selection([('new', 'New'),
                                   ('inprogress', 'In progress'),
                                   ('onhold', 'On Hold'),
                                   ('resolved','Resolved'),
                                   ('closed', 'Closed'),
                                   ('cancelled', 'Cancelled')], default='new',group_expand='_expand_states', index=True)

    info_impact = fields.Many2one('info.incident.impact', string="Impact")
    # role_id = fields.Many2one('info.res.users', related="info_assignement_group_id.info_group_id" )

    info_urgency = fields.Many2one('info.incidents.priority', string="Urgency")

    info_priority = fields.Many2one('info.incidents.urgency', string="Priority")

    info_assignement_group_id = fields.Many2one('info.assign.groups',string="Assignment group", required=True)
    info_assigned_to = fields.Many2one('res.users',string="Assigned to", required=True)

    info_short_desc = fields.Char(string="Short description")
    info_desc = fields.Text(string="Description")

    info_closed_ticket_id = fields.Many2one('info.closed.ticket', default=lambda self: self.env['info.closed.ticket'].search([], limit=1))
    info_closed_ticket = fields.Integer(related= 'info_closed_ticket_id.info_days')
    # calculated_close_ticket_day = fields.Date()
    calculated_d = fields.Date()


    # info_skills_id = fields.One2many('info.incidents.skills', 'skills_id', string="Skills")

    info_reason = fields.Selection([ ('notdef', 'Not defined'),
                                     ('caller', 'Awaiting Caller'),
                                     ('change', 'Awaiting Change'),
                                     ('problem', 'Awaiting Problem'),
                                     ('vendor','Awaiting Vendor')],string="Reason on Hold",default="notdef")      

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

    @api.onchange('info_state')
    def on_change_state(self):
        for record in self:
            if record.info_state ==  'resolved':
                # current_date = datetime.now().days()
                current_date = datetime.now().date()
                _logger.warning("------------THIS WAS CHANGED TO RESOLVED-----------")
                # current_day_date = current_date.days()
                _logger.warning(current_date)
                # self.calculated_close_ticket_day = current_day_date + self.info_closed_ticket
                date_1 = datetime.strptime(str(current_date), "%Y-%m-%d") 
                calculated_close = date_1 + timedelta(days=self.info_closed_ticket)
                self.calculated_d = calculated_close.date()
                _logger.warning(calculated_close)

    # @api.multi
    # def state_rel(self):
    #   for incident in self:
    #     self.info_state_re = self.state_rel