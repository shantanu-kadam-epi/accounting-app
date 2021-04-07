// Copyright (c) 2016, Bloomstack and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Account Trial Balance"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"account",
			"label": __("Account"),
			"fieldtype": "Link",
			"options": "Account ac"			
		},
		{
			"fieldname":"party_type",
			"label": __("Party Type"),
			fieldtype: "Select",
			options: [
				{ "value": "Customer", "label": __("Customer") },
				{ "value": "Suplier", "label": __("Suplier") },
			],		
		}
		
	]
};
