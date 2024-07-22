from odoo import models, fields, api, _
# from odoo.exceptions import UserError, ValidationError


class InheritResUser(models.Model):
    _inherit = "res.users"
    _description = """ Inherit_Res_User """

    property_ids = fields.One2many(comodel_name="real.estate", inverse_name="salesperson_id", string="Property")
    # property_ids = fields.Integer()