from odoo import models, fields


def _default_date(self):
    return fields.Date.today()


class RealEstate(models.Model):
    _name = "real.estate"
    _description = """ Test Model"""

    active = fields.Boolean(default=True)
    name = fields.Char(default="House", required=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        default="new",
        copy=False
    )
    description = fields.Text()
    postcode = fields.Char()

    # can write the one line method in the field defination, or call method
    date_availability = fields.Date(default=_default_date, copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(read_only=True, copy=False)
    bedrooms = fields.Integer(defult=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')
        ],
        required=True,
        default="north"
    )
