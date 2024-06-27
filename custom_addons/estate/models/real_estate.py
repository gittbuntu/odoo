from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


def _default_date(self):
    return fields.Date.today()


class RealEstate(models.Model):
    _name = "real.estate"
    _description = """ Test Model"""
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price >= 0)", "Expected price should be positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "Selling price should be positive")
    ]
    _order = "id desc"

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
    expected_price = fields.Float()
    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer(default=2)
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

    @api.onchange("garden")
    def _onchange_garden(self):
        for rec in self:
            if not rec.garden:
                rec.garden_area = 0

    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        for rec in self:
            date = fields.Date.today()
            print("date :", date)
            if rec.date_availability < date:
                rec.date_availability = date
                return {
                    'warning': {
                        'title': _("Warning"),
                        'message': _("Its can't be changeable")
                    }
                }

    def action_for_property_sold(self):
        for rec in self:
            if rec.state == "canceled":
                raise UserError(_("Canceled property can't be sold"))
            else:
                rec.state = "sold"

    def action_for_property_cancel(self):
        for rec in self:
            if rec.state == "sold":
                raise UserError(_("Sold property can't be canceled"))
            else:
                rec.state = "canceled"
