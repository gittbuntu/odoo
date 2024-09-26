from odoo import http


class HelloApi(http.Controller):
    @http.route('/api', auth='public', website=False, csrf=False, type='json', methods=['GET', 'POST'])
    def hello(self, **kwargs):
        contact_user = http.request.env['res.partner'].sudo().search([('id', '=', kwargs['id'])])
        if contact_user:
            contact_user.write({
                'name': kwargs['name']
            })
        else:
            http.request.env['res.partner'].sudo().create({'name': kwargs['name']})

        # E.g
        # contacts = http.request.env['res.partner'].sudo().search([])
        # # print(contacts)
        # contact_list = []
        # for contact in contacts:
        #     contact_list.append({
        #         'name': contact.name,
        #         'email': contact.email,
        #     })

        # return contact_list
        return kwargs
