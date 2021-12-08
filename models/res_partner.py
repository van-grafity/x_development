from odoo import api, fields, models
from odoo.tools.translate import _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
import string
from odoo.addons import decimal_precision as dp
import time
import requests
import math
from ast import literal_eval
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import math

class ResPartner(models.Model):
    _inherit = "res.partner"

    is_investor = fields.Boolean('Investor', default=False)
    investor_percent = fields.Integer('Investor Percent')

    def show_app_investor_percent_wizard(self):
        context = {
            'default_name' : self.id
        }

        action = {
            'name': _('Investor Percent'),
            'res_model': 'app.investor.percent.wizard',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target':'new',
            'context': context,
        }

        return action
