# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
            Open Academy module for managing trainings:
                - training courses
                - training sessions
                - attendees registration
        """,

    'author': "Open Academy Company",
    'website': "http://www.openacademy.com",

    'category': 'Open Academy',
    'version': '0.27',

    'depends': ['base'],

    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_views.xml',
        'views/partner_views.xml',
        'wizard/wizard_views.xml',
    ],

    'demo': [
        'data/openacademy_course_demo.xml',
    ],
}
