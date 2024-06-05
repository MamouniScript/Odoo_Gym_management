from odoo import fields, models

class Schedule(models.Model):
    _name = 'mana_gym.schedule'
    _description = 'Class Schedule'

    class_id = fields.Many2one('mana_gym.class', string='Class')
    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ], string='Day')
    time = fields.Float(string='Time')
    location = fields.Char(string='Location')