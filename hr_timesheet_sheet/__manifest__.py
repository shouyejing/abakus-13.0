# Copyright 2018 Eficent
# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'HR Timesheet Sheet',
    'version': '11.0.2.0.1',
    'category': 'Human Resources',
    'sequence': 80,
    'summary': 'Timesheet Sheets, Activities',
    'license': 'AGPL-3',
    'author': 'Eficent, Onestein, Odoo Community Association (OCA), ABAKUS IT-SOLUTIONS',
    'website': 'https://github.com/OCA/hr-timesheet',
    'depends': [
        'hr_timesheet',
        'web_widget_x2many_2d_matrix',
        'hr_analytic_timesheet_improvements',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_timesheet_sheet_security.xml',
        'data/hr_timesheet_sheet_data.xml',
        'views/hr_timesheet_sheet_views.xml',
        'views/hr_department_views.xml',
        'views/res_config_settings_views.xml',
        'templates/assets.xml',
    ],
    'installable': True,
    'auto_install': False,
}
