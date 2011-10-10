# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2010 Vauxoo C.A. (http://openerp.com.ve/) All Rights Reserved.
#                    Javier Duran <javier@vauxoo.com>
#                    Nhomar Hernandéz <nhomar@vauxoo.com>
# 
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    "name" : "Due report For Venezuela",
    "version" : "0.1",
    "depends" : ["account","retencion_iva","retencion_municipal","retencion_islr",],
    "author" : "Vauxoo",
    "description" : """
    What this module does:
    --    Build the due report analisys from an administrative point of view.
    --    Check all invoice and its payments.
    --    Filter Retentions about ISLR, IVA and Municipal.
    Give a presentable report for Banks.
    """,
    "website" : "http://openerp.com.ve",
    "category" : "Generic Modules/Accounting",
    "init_xml" : [
    ],
    "demo_xml" : [
    ],
    "update_xml" : [
        "overdue_report.xml",
        "overdue_wizard.xml",
    ],
    "active": False,
    "installable": True,
}