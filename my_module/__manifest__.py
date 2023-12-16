{
    'name': 'My Module',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/my_module_security.xml',
        'views/my_model_views.xml',
        'views/other_model_views.xml',
        'data/my_module_data.xml',
    ],
    'demo': [
        'data/my_module_demo.xml',
    ],
    'installable': True,
    'application': True,
}
