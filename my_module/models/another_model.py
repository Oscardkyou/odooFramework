# structure_v1/now/models/another_model.py
from odoo import models, fields, api

class AnotherModel(models.Model):
    _name = 'my.module.another_model'
    _description = 'Another Model'

    name = fields.Char(string='Act Name', required=True)
    date = fields.Date(string='Date', required=True)
    status = fields.Selection([('purchase', 'Purchase'), ('sale', 'Sale')], string='Status')
    apply_for_products_from = fields.Many2one('stock.location', string='Apply for products from')
    assign_new_warehouse = fields.Many2one('stock.location', string='Assign new warehouse')
    products = fields.One2many('my.module.product', 'act_id', string='Products')

class MyModuleProduct(models.Model):
    _name = 'my.module.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    expenses_revenues = fields.One2many('my.module.expense.revenue', 'product_id', string='Expenses/Revenues')

class MyModuleExpenseRevenue(models.Model):
    _name = 'my.module.expense.revenue'
    _description = 'Expense/Revenue'

    category = fields.Char(string='Category', required=True)
    amount = fields.Float(string='Amount', required=True)
    product_id = fields.Many2one('my.module.product', string='Product')
