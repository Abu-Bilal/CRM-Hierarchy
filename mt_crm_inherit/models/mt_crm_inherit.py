from odoo import models,api

class MtCrmInherit(models.Model):
    _inherit= 'crm.lead'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        user = self.env.user
        if user.has_group('mt_crm_inherit.crm_team_leader'):
            args = [('|', ('user_id', '=', user.id), ('team_id.user_id', '=', user.id))] + args
        return super(MtCrmInherit, self).search(args, offset, limit, order, count)