from odoo import models, fields, api


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
    property_type_id = fields.Many2one("real.estate.property.type")
    offer_ids = fields.One2many(comodel_name="real.estate.property.offer", inverse_name="property_id", string="offers")
    tag_ids = fields.Many2many("real.estate.property.tag")

    total_area = fields.Float(compute='_total_area')  # by default its readonly
    # we can create compute field depends on another model.field by using mapped function
    best_price = fields.Float(compute='_best_price', default=0)

    @api.depends('living_area', 'garden_area')
    def _total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    @api.depends('offer_ids.price')
    def _best_price(self):
        for rec in self:
            # this
            # rec.best_price = max(rec.offer_ids.mapped('price')) if rec.offer_ids else 0
            # or this both ways produce same result
            if rec.offer_ids:
                rec.best_price = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_price = 0
