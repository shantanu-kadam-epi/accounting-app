# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bloomstack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AccountPurchaseInvoice(Document):
    def on_submit(self):
        Payment_entry = frappe.new_doc('Account Payment Entry')
        Payment_entry.party_name = self.suplier_name
        Payment_entry.payment_type = self.payment_type			          
        Payment_entry.party_type = 'Suplier'			          
        Payment_entry.payment_mode = self.payment_mode			          
        Payment_entry.date = self.date			          
        Payment_entry.purchase_invoice_no = self.name   
        Payment_entry.account_details = self.account_no   
        Payment_entry.save()
        Payment_entry.submit()
        Journal_entry = frappe.new_doc('Account Journal Entry')        		          
        Journal_entry.account_details = self.account_no		          
        Journal_entry.party = self.suplier_name		          
        Journal_entry.posting_date = self.date			          
        Journal_entry.total_amount = self.total_amount			          
        Journal_entry.entry_type = 'journal entry'			          
        Journal_entry.save()
        Journal_entry.submit()

        