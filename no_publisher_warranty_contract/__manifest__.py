# -*- coding: utf-8 -*-
{
    'name': "Bypass publisher Warranty Contract",

    'summary': """Bypass publisher Warranty Contract""",

    'description': """
        This module will enable you to use Odoo enterprise for free.
    """,

    'author': "Babatope Ajepe",
    'website': "https://ajepe.github.io",

    'category': 'Hidden',
    'version': '0.1',

    'depends': ['base', 'mail'],

    'auto_install': True,
    'license': 'GPL-2',

    # always loaded
    'data': [
        'data/ir_cron_data.xml',
    ],

    #"pre_init_hook": "run_pre_init_hook",
    "pre_init_hook": "run_post_init_hook",
}

