from odoo import fields, models, _

class Customer(models.Model):
    _name="customer.model"

    customer_model_id = fields.Many2one('xdev.rental')
    name = fields.Char('Customer Name')
    identity_number = fields.Char('No. Identity')
    email = fields.Char('email')
    phone_number= fields.Char('No. Phone')
    address = fields.Char('Address')
    username = fields.Char('Username')
    password = fields.Char('Password')