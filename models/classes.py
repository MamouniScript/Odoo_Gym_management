from odoo import fields, models

class Classes(models.Model):
    _name = 'mana_gym.class'
    _description = 'Fitness Class'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    duration = fields.Integer(string='Duration (minutes)')
    max_capacity = fields.Integer(string='Maximum Capacity')
    trainer_id = fields.Many2one('mana_gym.trainer', string='Trainer')
    schedule_ids = fields.One2many('mana_gym.schedule', 'class_id', string='Schedules')
    location = fields.Char(string='Location')