from odoo import fields, models

class Membership(models.Model):
    _name = 'mana_gym.membership'
    _description = 'Gym Membership'

    name = fields.Char(string='Membership Type', required=True)
    duration = fields.Integer(string='Duration (months)')
    price = fields.Float(string='Price')
