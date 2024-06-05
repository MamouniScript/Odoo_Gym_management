from odoo import fields, models

class Trainer(models.Model):
    _name = 'mana_gym.trainer'
    _description = 'Fitness Trainer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    specialization = fields.Char(string='Specialization')
    certification_details = fields.Text(string='Certification Details')
    hourly_rate = fields.Float(string='Hourly Rate')
