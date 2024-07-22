from odoo import models, fields, api, _

class MyFirstApp(models.Model):
    _name = "my.first.app"
    _description = """ For Learning """

    name = fields.Char()
    long_text = fields.Text()
    an_integer = fields.Integer()
    an_float = fields.Float()
    an_bool = fields.Boolean()
    a_date = fields.Date()
    a_datetime = fields.Datetime()
    a_slection = fields.Selection([('option1', 'option1'), ('option2', 'option2')])
    a_html = fields.Html()
    a_binary = fields.Binary()
    an_image = fields.Image()


    