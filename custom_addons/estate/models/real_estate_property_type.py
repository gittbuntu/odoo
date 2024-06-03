from odoo import fields, models

class Real_Estate_Property_Type(models.Model):
    _name = "real.estate.property.type"
    _description = """ Test Model"""

    name = fields.Char(string="Name", required=True)