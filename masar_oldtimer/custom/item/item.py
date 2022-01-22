from __future__ import unicode_literals
import frappe, erpnext, json

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def second_category_query(doctype, txt, searchfield, start, page_len, filters):
	vrcategory = filters.get('first_category')
	return frappe.db.sql("""
		SELECT second_category
		FROM `tabItem Second Category`
		WHERE first_category = '%s'
		"""%(vrcategory)
	)

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def third_category_query(doctype, txt, searchfield, start, page_len, filters):
	vrfirstcategory = filters.get('first_category')
	vrsecondcategory = filters.get('second_category')
	return frappe.db.sql("""
		SELECT third_category
		FROM `tabItem Third Category`
		WHERE first_category = '%s' AND second_category = '%s'
		"""%(vrfirstcategory,vrsecondcategory)
	)
