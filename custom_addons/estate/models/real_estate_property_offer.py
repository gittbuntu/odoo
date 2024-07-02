from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class Real_Estate_Property_Offer(models.Model):
    _name = "real.estate.property.offer"
    _description = "Offer made"
    _sql_constraints = [
        ("check_price", "CHECK(price >= 0)", "Offer price should be positive")
    ]
    _order = "price desc"

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

    @api.constrains("price")
    def _constraint_selling_price(self):
        for rec in self:
            if rec.price < (rec.property_id.expected_price * 90) // 100:
                raise ValidationError(_("Price should be equal to or greater then 90% of expected price."))

    def create(self, vals_list):
        for val in vals_list:
            browsable_id = self.env["real.estate"].browse(val["property_id"])
            print("val :", val)
            print("browsable_id :", browsable_id[0]["state"])
            # print("browsable_id :", browsable_id[0]["offer_ids"]["price"])
            offer_price_list = [0]
            for rec in browsable_id[0]["offer_ids"]:
                offer_price_list.append(rec[0]["price"])
            # print(offer_price_list)
            # print(max(offer_price_list))
            offer_price = max(offer_price_list)
            if val["price"] < offer_price:
                #         # if val["price"] < browsable_id[0]["offer_ids"]["price"]:
                raise UserError(_(f"{val['price']} is not valid must be greater then {offer_price}"))
            else:
                #     browsable_id.state = "received"
                browsable_id[0]["state"] = "received"
                return super().create(vals_list)
        # #     return super().create(vals_list)
