# Copyright 2020 Manish Kumar Bohra <manishbohra1994@gmail.com> or <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Bulk Sales Order Confirmation',
    'version': '1.0',
    'summary': 'This app allows you to confirm multiple sales order in bulk',
    'description': 'This app allows you to confirm multiple sales order in bulk',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'license': 'LGPL-3',
    "data": [
        'views/bulk_sales.xml',
    ],
    'images': ['static/description/bulk.gif'],
    'depends': ['sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,

}
