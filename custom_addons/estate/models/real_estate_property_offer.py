from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Real_Estate_Property_Offer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Offer made"

    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused")
        ]
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("real.estate", required=True)
    type_id = fields.Many2one(related='property_id.property_type_id', store=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_date_deadline", inverse="_validity")

    @api.depends("validity")
    def _date_deadline(self):
        for rec in self:
            # the create_date is only filled in when the record is created
            # rec.date_deadline = rec.create_date + relativedelta(days=rec.validity)

            # so we will use this way
            rec.date_deadline = fields.Date.today() + relativedelta(days=rec.validity)

    @api.depends("date_deadline")
    def _validity(self):
        for rec in self:
            rec.validity = (rec.date_deadline - fields.Date.today()).days
            print(rec.validity)

    def action_for_accept(self):
        for rec in self:
            if "accepted" in rec.property_id.offer_ids.mapped("status"):
                raise UserError(_("Hi ; Offer already accepted"))
            else:
                rec.status = "accepted"
                rec.property_id.selling_price = rec.price
        return True

    def action_for_refuse(self):
        for rec in self:
            rec.status = "refused"
        return True
