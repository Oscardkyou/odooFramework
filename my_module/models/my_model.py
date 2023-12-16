# structure_v1/now/models/my_model.py
from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.module.model'
    _description = 'My Module Model'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    # Добавьте другие поля по необходимости
