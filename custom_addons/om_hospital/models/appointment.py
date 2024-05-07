from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    ref = fields.Char(string='Reference')
    # if we want to get default values in any field then use default="anything",
    # for date we use default=fields.Date.context_today and for datetime we use default=fields.Datetime.now
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)

    # if we want to create related field then we use related attribute(by default related fields are readonly but if
    # we want to be add then add attribute readonly=False but changes in this field also change value of
    # its parent model)
    # gender = fields.Selection([('male', 'Male'), ('female',
    # 'Female')], string="Gender", related='patient_id.gender') (both are working)
    gender = fields.Selection(related='patient_id.gender')

    # Note : there is a difference between related field and onchange field
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
