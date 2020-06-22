# Copyright 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# Copyright 2018 David Vidal - <david.vidal@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Email tracking",
    "summary": "Email tracking system for all mails sent",
    "version": "11.0.3.2.1",
    "category": "Social Network",
    "website": "http://github.com/OCA/social",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "decimal_precision",
        "mail",
    ],
    "data": [
        "data/tracking_data.xml",
        "security/mail_tracking_email_security.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/mail_tracking_email_view.xml",
        "views/mail_tracking_event_view.xml",
        "views/mail_message_view.xml",
        "views/res_partner_view.xml",
        "wizard/mail_compose_message_view.xml",
    ],
    "qweb": [
        "static/src/xml/mail_tracking.xml",
        "static/src/xml/failed_message.xml",
        "static/src/xml/client_action.xml",
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "pre_init_hook": "pre_init_hook",
}