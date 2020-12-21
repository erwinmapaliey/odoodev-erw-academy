from odoo import api, fields, models


class AttendeeWizard(models.TransientModel):
   _name = 'academy.attendee.wizard'
   _description = 'Popup to adding Attendee Data'

   def _default_session(self):
      return self.env['academy.session'].browse(self._context.get('active_id'))

   session_id   = fields.Many2one( comodel_name="academy.session", string="Sesi Kursus", default = _default_session, required = True )
   attendee_ids = fields.Many2many( comodel_name="res.partner", string="Student", domain="[('is_student', '=', True)]" )

   def action_subscribe(self):
      vals = []
      if self.attendee_ids:
         for attd in self.attendee_ids:
            data = {
               'name': 'No Pendaftaran',
               'session_id': self.session_id.id,
               'student_id': attd.id,
            }
         vals += [(0,0, data)]
      self.session_id.attendee_ids = vals
