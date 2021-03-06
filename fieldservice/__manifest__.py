# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service',
    'summary': 'Locations, Orders, Calls',
    'version': '11.0.0.0.1',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/field-service',
    'depends': [
        'base_geolocalize',
        'mail',
        'web_timeline',
    ],
    'data': [
        'data/ir_sequence.xml',
        'data/mail_message_subtype.xml',
        'data/module_category.xml',
        'data/fsm_stage.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/fsm_stage.xml',
        'views/fsm_tag.xml',
        'views/res_partner.xml',
        'views/fsm_location.xml',
        'views/fsm_person.xml',
        'views/fsm_vehicle.xml',
        'views/fsm_order.xml',
        'views/fsm_route.xml',
        'views/menu.xml',
        'wizard/fsm_wizard.xml',
    ],
    'application': True,
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'wolfhall',
        'max3903',
    ],
}
