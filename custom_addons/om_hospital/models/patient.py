from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True) # if we want to tracke any field data then place tracking=true
    age = fields.Integer(string='Age')
    ref = fields.Char(string='Reference')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender") #this field is used for multiple selections
    
    active = fields.Boolean(string="Active", default=True) # creation of this field is mendatory for active archive button
