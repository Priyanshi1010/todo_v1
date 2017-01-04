# -*- coding: utf-8 -*-
from openerp import models,fields,api
class TodoTask(models.Model):
	#model added to our custom module
	_name = 'todo.task' #attribute used to refer this model name as
	name = fields.Char('Description',required=True) #name of record
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?',default=True) #showing only active records
	#python decorators to add buttons
	@api.one
	def do_toggle_done(self):
		self.is_done = not self.is_done
		return True
	@api.multi
	def do_clear_done(self):
		done_recs = self.search([('is_done','=',True)])
		done_recs.write({'active':False})
		return True

