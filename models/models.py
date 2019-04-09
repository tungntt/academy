# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class academy(models.Model):
#     _name = 'academy.academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Project study: Open Academy Courses'

    name = fields.Char(string="Title", required=True)
    description = fields.Text