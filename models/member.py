from odoo import fields, models

class Member(models.Model):
    _name = 'mana_gym.member'
    _description = 'Gym Member'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    membership_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Membership Status', default='active')
    membership_type_id = fields.Many2one('mana_gym.membership', string='Membership Type')
    joining_date = fields.Date(string='Joining Date')
