# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Filtrar Ordenes POS',
    'version': '0.1',
    'description': """
Filtrar Ordenes POS
========================================================================
* Incluye botón en ficha del cliente para ver las oŕdenes de PdV propias
* Traducir a español de campo Debt en ficha del cliente
    """,
    'category': 'Point of Sale',
    'author': 'Alexander Rodriguez',
    'website': '',
    'depends': ['base','pos_debt_notebook'],
    'data': [
            'point_of_sale_view.xml',
            'res_partner_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: