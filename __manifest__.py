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
