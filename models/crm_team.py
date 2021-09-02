from odoo import api, fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    member_ids = fields.Many2many('res.users', 'crm_team_res_users_rel',
                                  'crm_team_id', 'res_users_id', 'Team Members')
