###################################################################################
#
#    Template Email
#
###################################################################################
from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__) 

class emailtemplateIncident(models.Model):
    _name = 'info.email.template.incident'

    """Fileds Declaration
       ------------------
       name : Template name 
       email = HTML body of email
       """

    name = fields.Char(string="Email template name")
    email = fields.Html(string="Email body")