from odoo import models, fields

class Real_Estate_Property_Tag(models.Model):
    _name = "real.estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(required=True)
