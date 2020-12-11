from odoo import api, fields, models

class CourseCategory(models.Model):
   _name        = 'academy.course.category'
   _description = 'Course Category'

   name        = fields.Char( string = 'Course Category', required = 'True' )
   description = fields.Text( string = 'Description' )
   active      = fields.Boolean( string = 'Active', default = True )
   course_ids  = fields.One2many( comodel_name='academy.course', inverse_name='category_id', string='Course' )
   