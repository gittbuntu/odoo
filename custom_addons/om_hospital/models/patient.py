from datetime import date
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    # if we want to track any field data then place tracking=true
    name = fields.Char(string='Name', tracking=True)
    # this age field is just normal integer filed but it can be make as computed field
    # age = fields.Integer(string='Age')
    # Note : computed field can't be set in filter or group_by because they can't save in
    # database by default it can be stored by set attribute of stored = True
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    dob = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference')

    # this field is used for multiple selections
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")

    # creation of this field is mendatory for active archive button
    active = fields.Boolean(string="Active", default=True)

    @api.depends('dob')
    def _compute_age(self):
        # iterate record one by for preventing singleton error
        for rec in self:
            if rec.dob:
                today = date.today()
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0
