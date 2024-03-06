# Copyright © 2024 Garazd Creation (https://garazd.biz)
# @author: Yurii Razumovskyi (school@garazd.biz)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 4-1: Views, Actions, Menus',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Odoo School Lesson 4-1: Views, Actions, Menus.""",
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'school_lesson_3_7',
    ],
    'data': [
        'views/school_lesson_menus.xml',
        'views/social_subscriber_views.xml',
    ],
    'demo': [
        'data/social_subscriber_demo.xml',
    ],
    'support': 'school@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
