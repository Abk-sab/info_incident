# -*- coding: utf-8 -*-
{  
    'name': 'Info Incident',
    'version': '12.0',

    # 'category': 'Accounting',
    'author': 'Kit-Tech',
    'summary': 'Info Incident',
    # 'website': 'https://github.com/fmdl',

    'depends': ['base','board','hr','info_knowledge','mail',],
    'data': [

             'security/user_groups.xml',   
             'security/ir.model.access.csv',  
             'views/info_incident.xml',
             'views/info_incident_category.xml',
             'views/info_incident_user.xml',
             'views/assigne_group.xml',
             'views/closed_ticket.xml',
             'views/info_incident_tags.xml',
             'views/info_incident_close_codes.xml',
             'views/impact.xml',
             'views/priority.xml',
             'views/urgency.xml',
             'views/incident_email_template.xml',
             'data/data.xml',

            ],
    'qweb': [
        # 'static/src/xml/knowledge_info_kanban_template.xml',
        ],
    'demo': [],
    'license': 'LGPL-3',
    # 'support': 'https://github.com/fmdl',
    'installable': True,
    'auto_install': False,
    # 'price': 0.0,
    # 'currency': 'EUR',
    'sequence': 1,
    # 'images': ['images/main_screenshot.png'],
}
