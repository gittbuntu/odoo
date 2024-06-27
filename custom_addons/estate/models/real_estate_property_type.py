from odoo import fields, models, api, _


class Real_Estate_Property_Type(models.Model):
    _name = "real.estate.property.type"
    _description = """ Test Model"""
    _sql_constraints = [
        ("check_property_type_name", "UNIQUE(name)", "Name should be unique.")
    ]
    _order = "name"
    sequence = fields.Integer(default=1)

    name = fields.Char(string="Name", required=True)
    property_type_ids = fields.One2many(comodel_name="real.estate", inverse_name="property_type_id", string="offers")
    property_count = fields.Integer(compute="_compute_property_count")
    offer_ids = fields.One2many(comodel_name="real.estate.property.offer", inverse_name="type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends("property_type_ids")
    def _compute_property_count(self):
        for rec in self:
            rec.property_count = len(rec.property_type_ids)

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    def action_state_property_type_ids(self):
        return {
            "name": _("Related Properties"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "real.estate",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id}
        }

    def action_state_real_estate_property_offer(self):
        return {
            "name": _("Related Properties"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "real.estate.property.offer",
            "target": "current",
            "domain": [("type_id", "=", self.id)],
        }
