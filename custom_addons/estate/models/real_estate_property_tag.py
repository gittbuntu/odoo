from odoo import models, fields

class Real_Estate_Property_Tag(models.Model):
    _name = "real.estate.property.tag"
    _description = "Property Tag"
    _sql_constraints = [
        ("check_tag_name", "UNIQUE(name)", "Name should be unique.")
    ]
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")
