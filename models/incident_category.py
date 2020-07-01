# -*- coding: utf-8 -*-
###################################################################################
#
#    Incident category and subcategory Model and functions
#
###################################################################################

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__) 


class InfoIncidentCategory(models.Model):
    _name = 'info.incidents.category'
    _description = 'Category'

    name = fields.Char(string="Name")
    info_description =fields.Text(string="Description")
    info_subcat_ids = fields.One2many(comodel_name='info.incidents.subcategory', inverse_name='info_subcat_id',
                                        string="Subcategory")
    color = fields.Integer('color index', default=0)
   
class InfoIncidentScategory(models.Model):
    _name = 'info.incidents.subcategory'
    _description = 'Subcategory'

    name = fields.Char(string="Name")
    info_description =fields.Text(string="Description")
    info_subcat_id = fields.Many2one(comodel_name='info.incidents.category', string="Parent category")
    info_subcat_incident_id = fields.Many2one(comodel_name='info.incidents.incidents')