from odoo import api, fields, models


class Session(models.Model):
   _name = 'academy.session'
   _description = 'Data Course Session'

   name          = fields.Char( string = 'Name' )
   course_id     = fields.Many2one( comodel_name='academy.course', string = 'Course' )
   instructor_id = fields.Many2one( comodel_name='res.partner', string = 'Instructor', domain = "[('is_instructor', '=', 'True')]" )
   session_date  = fields.Datetime( string = 'Session Date', default = fields.Datetime.now() )
   min_attendee  = fields.Integer( string = 'Minimum Attendee' )
   
   
