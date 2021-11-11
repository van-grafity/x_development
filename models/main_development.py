from odoo import fields, models, _

class MainDevelopment(models.Model):
    _name = "main.development"

    name = fields.Char('Nama')
    