from odoo import api, fields, models

class Course(models.Model):
   _name        = 'academy.course'
   _description = 'Data Course'

   name        = fields.Char( string = 'Course Name', required = 'True', help = "Fill course name..." )
   description = fields.Text( string = 'Description' )
   category_id = fields.Many2one( comodel_name = 'academy.course.category', string = 'Course Category', required = True )
   active      = fields.Boolean( string = 'Active', default = True )