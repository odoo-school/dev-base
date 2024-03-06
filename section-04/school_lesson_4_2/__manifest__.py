# Copyright © 2024 Garazd Creation (https://garazd.biz)
# @author: Yurii Razumovskyi (school@garazd.biz)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 4-2: List Views',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Odoo School Lesson 4-2: List (Tree) Views.""",
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'school_lesson_4_1',
    ],
    'data': [
        'views/social_subscriber_views.xml',
    ],
    'support': 'school@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
