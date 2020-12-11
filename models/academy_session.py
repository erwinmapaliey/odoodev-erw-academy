from odoo import api, fields, models


class Session(models.Model):
   _name        = 'academy.session'
   _description = 'Data Course Session'

   name          = fields.Char( string = 'Name' )
   course_id     = fields.Many2one( comodel_name='academy.course', string = 'Course' )
   instructor_id = fields.Many2one( comodel_name='res.partner', string = 'Instructor', domain = "[('is_instructor', '=', 'True')]" )
   session_date  = fields.Datetime( string = 'Session Date', default = fields.Datetime.now() )
   min_attendee  = fields.Integer( string = 'Minimum Attendee' )
   attendee_ids  = fields.One2many( comodel_name = 'academy.course.attendee', inverse_name = 'session_id', string = 'Attendee' )

class Attendee(models.Model):
   _name        = 'academy.course.attendee'
   _description = 'Attendee of Course Session'

  name          = fields.Char( string = 'Name' )
  student_id    = fields.Many2one( comodel_name = 'res.partner', string = 'Student', domain = "[('is_student', '=', 'True')]" )
  register_date = fields.Datetime( string = 'Registration Date', default = fields.Datetime.now() )
  session_id    = fields.Many2one( comodel_name = 'academy.session', string = 'Session' )
  remark        = fields.Char( string = 'Remark' )