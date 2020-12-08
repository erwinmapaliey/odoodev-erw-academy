# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Course(models.Model):
   _name        = 'academy.course'
   _description = 'Data Course'

   name        = fields.Char( string = 'Course Name', required = 'True', help = "Fill course name..." )
   description = fields.Char( string = 'Description' )
   active      = fields.Boolean( string = 'Active', default = True )