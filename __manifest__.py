# -*- coding: utf-8 -*-
{
    'name': "ManaGym by Mamouni",

    'summary': """
        SI pour la gestion des salles de sports""",

    'description': """
        Ce systéme gére et supervise une salle de sport, y compris ces équipements, abonnements, clients, payements, ...etc.
    """,

    'author': "Mamouni",
    'website': "https://www.yourcompany.com",

    'category': 'Services',
    'version': '0.1',

    'images': ['static/description/icon.png'],

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'hr', 'web', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/member_views.xml',
        'views/trainer_views.xml',
        'views/classes_views.xml',
        'views/schedule_views.xml',
        'views/equipement_views.xml',
        'views/membership_views.xml',
        'views/payement_views.xml',
        'views/menus.xml',
        'report/report_views.xml',
        'views/ppt.xml',
    ],


    'installable': True,
    'application': True,
}
