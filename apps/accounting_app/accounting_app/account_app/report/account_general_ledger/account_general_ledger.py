#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, gvn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _, _dict
from frappe.utils import getdate, flt
import frappe
from frappe.utils import datetime


def execute(filters=None):
    if not filters:
        return ([], [])

      # validations

    if filters.from_date > filters.to_date:
        frappe.throw(_('From Date must be before To Date'))

    columns = get_columns()
    data = get_data(filters)

    return (columns, data)


def get_data(filters):
    if (filters.get('account') or filters.get('to_date') or filters.get('from_date')):        
        query = 'select * from `tabAccount Journal Entry` {} order by posting_date desc'.format(conditions(filters))
        print(query)        
        data = frappe.db.sql(query, filters, as_dict=1)
        return data
    else:        
        query = 'select * from `tabAccount Journal Entry` order by posting_date desc'
        data = frappe.db.sql(query, as_dict=1)

    return data

def conditions(filters):    
    account = filters.get('account')
    from_date = filters.get('from_date')
    to_date = filters.get('to_date')
    conditions = []

    if not (to_date and from_date):
        from_date = datetime.MINYEAR
        to_date = datetime.datetime.today()
    else:
        conditions += ["posting_date >= '{}' and posting_date <= '{}'".format(from_date, to_date)]       
    
    if filters.get('account'):
        conditions += ["account_details = '{}'".format(account)]

    where_conditions = 'where {}'.format(' and '.join(conditions))    
    return where_conditions

def get_columns():
    columns = [
        {
        'label': 'ID',
        'fieldname': 'name',
        'fieldtype': 'Link',
        'options': 'Account Journal Entry',
        'width': 180,
        },{
        'label': 'Account',
        'fieldname': 'account_details',
        'fieldtype': 'Link',
        'options': 'Account ac',
        'width': 180,
        },{
        'label': 'Party',
        'fieldname': 'party',
        'fieldtype': 'Link',
        'options': 'Party',
        'width': 180,
        },{
        'label': 'Total Amount',
        'fieldname': 'total_amount',
        'width': 180,
        },{
        'label': 'Posting Date',
        'fieldname': 'posting_date',
        'fieldtype': 'Date',
        'width': 150,
        }]

    return columns
