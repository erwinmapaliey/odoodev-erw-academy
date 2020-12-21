from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class Session(models.Model):
   _name        = 'academy.session'
   _description = 'Data Course Session'

   name          = fields.Char( string = 'Name' )
   course_id     = fields.Many2one( comodel_name = 'academy.course', string = 'Course' )
   instructor_id = fields.Many2one( comodel_name = 'res.partner', string = 'Instructor', domain = "[('is_instructor', '=', 'True')]" )
   session_date  = fields.Datetime( string = 'Session Date', default = fields.Datetime.now(), required = True)
   min_attendee  = fields.Integer( string = 'Minimum Attendee' )
   description   = fields.Text( string = 'Description' )
   attendee_ids  = fields.One2many( comodel_name = 'academy.session.attendee', inverse_name = 'session_id', string = 'Attendee')   
   taken_seats   = fields.Float( compute = '_compute_taken_seat', string = 'Taken Seats', store = True)
   state         = fields.Selection( string = 'State', selection = [('draft', 'Draft'), ('valid', 'Valid'), ('cancel', 'Cancel'),], readonly = True, required = True, default = 'draft')
   email         = fields.Char( string = 'Email', related = "instructor_id.email", store = True)

   def action_cancel(self):
      self.write({'state': 'cancel'})
   def action_valid(self):
      self.write({'state': 'valid'})
   def action_reset(self):
      self.write({'state': 'draft'})

   @api.depends('min_attendee', 'attendee_ids')
   def _compute_taken_seat(self):
      for record in self:
         if not record.min_attendee:
            record.taken_seats = 0.0
         else:
            record.taken_seats = 100.0 * len(record.attendee_ids) / record.min_attendee
   
   def unlink(self):
      for record in self:
         if record.state in ['valid', 'cancel']:
            raise UserError("Tidak bisa hapus data Valid dan Cancel!!")
      return super(Session, self).unlink()

   @api.onchange('min_attendee', 'attendee_ids')
   def _verify_seats_attendee(self):
      if self.min_attendee < 0:
         return {
            'warning':{
               'title'  : "Salah Data!",
               'message': "Min Attendee tidak boleh kurang dari O", 
            },
         }
      if self.min_attendee < len(self.attendee_ids):
         return {
            'warning' : {
               'title'  : "Too many attendees",
               'message': "Increase minimal attendee or remove excess attendees",
            }
         }

class SessionAttendee(models.Model):
   _name        = 'academy.session.attendee'
   _description = 'Course Session Attendee Data'

   name       = fields.Char( string = 'No. Pendaftaran' )
   student_id = fields.Many2one( comodel_name = 'res.partner', string = 'Student', domain = "[('is_student', '=', 'True')]" )
   reg_date   = fields.Datetime( string = 'Registation Date', default = fields.Datetime.now() )
   session_id = fields.Many2one( comodel_name = 'academy.session', string = 'Course Session' )
   remarks    = fields.Char( string = 'Remarks' )