from odoo import http


class MyController(http.Controller):

    @http.route('/school_lesson_4_6/hello', auth='user', type='json')
    def hello(self):
        return {
            'html': """
            <div class="oe_container bg-primary">
                <div class="oe_row p-4">
                    <div class="offset-4 col-4"><h1 class="text-center text-white">Hello, world</h1></div>
                </div>                    
            </div> """
        }
