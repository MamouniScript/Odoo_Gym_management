from odoo import fields, models

class Equipment(models.Model):
    _name = 'mana_gym.equipment'
    _description = 'Gym Equipment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity')
    condition = fields.Selection([
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    ], string='Condition')
    location = fields.Char(string='Location')