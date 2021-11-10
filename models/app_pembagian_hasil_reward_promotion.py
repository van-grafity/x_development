from odoo import api, fields, models

class AppPembagianHasilRewardPromotion(models.Model):
    _name = "app.pembagian.hasil.reward.promotion"

    # booking_id = fields.Many2one('pgs.booking.order', string='Booking ID')
    name_reward = fields.Char('Nama Hadiah')