# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Multi Currency payment in Odoo",
    "version" : "13.0.0.3",
    "category" : "point of sale",
    "depends" : ['base','point_of_sale'],
    "author": "BrowseInfo",
    "price": 29.00 ,
    'currency': "EUR",
    'summary': 'point of sales multiple currency app POS Multi Currency payment pos payment different currency allow multi currency payment on pos multiple currency payment in Point of Sale pay order with different currency Payment with Multi Currency',
    "description": """   
	odoo point of sale multi currency payment pos multicurrency payment pos multi currency payment 
	Odoo pos support multiple currency payment multiple currency in pos
	odoo multiple currency payment pos multi currency payment pos multi currency pos
	Odoo multiple currency pos multiple currency point of sales multiple currency setup pos 
	Odoo pos multiple currency setup multicurrency payment in pos odoo pos multi currency pricelist odoo
    odoo pos pricelist based on currency odoo pos multi currency pricelist on point of sale
    odoo point of sale multiple currency pricelist odoo pos multi currency pricelist odoo
    odoo multi currency payment odoo difference currency payment odoo payment with multiple currency
	
	  """,
    "website" : "www.browseinfo.in",
    "data": [
    'security/ir.model.access.csv',
        'views/assests.xml',
        'views/pos_config_inherit.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml'
    ],
    "auto_install": False,
    "installable": True,
    'live_test_url':'https://youtu.be/WfbpRH8sMUE',
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: