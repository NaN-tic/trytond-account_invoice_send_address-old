# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .invoice import  *


def register():
    Pool.register(
        Address,
        Invoice,
        Sale,
        module='account_invoice_send_address', type_='model')
