# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bloomstack and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.nestedset import NestedSet, get_root_of
from erpnext.utilities.transaction_base import delete_events
from frappe.model.document import Document

class test(Document):
	nsm_parent_field = 'parent_test'
