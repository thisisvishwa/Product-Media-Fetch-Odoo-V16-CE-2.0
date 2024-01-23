{
    'name': 'Product Media via URLs',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Fetch and display product media from external URLs',
    'author': 'Vishwa G',
    'website': 'https://thisis.com',
    'license': 'AGPL-3',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_media_url_config_views.xml',
        'views/templates.xml',
        'data/ir_cron_data.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/product_media_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'product_media_urls/static/src/js/product_media_script.js',
            'product_media_urls/static/src/css/product_media_style.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'description': """
Product Media via URLs Module for Odoo Version 16 Community Edition
==================================================================
This module allows dynamic fetching of product images and additional media from external URLs and displays them on the website without storing them in the Odoo database.
""",
}