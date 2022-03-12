from _future_ import unicode_literals
import frappe, erpnext, json
from frappe import _, scrub, ValidationError
from frappe.utils import flt, comma_or, nowdate, getdate
from erpnext.setup.utils import get_exchange_rate
from erpnext.accounts.general_ledger import make_gl_entries
from erpnext.controllers.accounts_controller import AccountsController
from frappe.model.document import Document

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def second_category_query(doctype, txt, searchfield, start, page_len, filters):
	vritem_code = filters.get('item_code')
	categories = filters.get('categories')
	categories_tuple = tuple(categories)
	if len(categories) != 1:
		return frappe.db.sql("""
			Select name,first_category
			From `tabItem Second Category` tisc
			Where first_category in {}""".format(categories_tuple) ,as_dict=True)
	else:
		return frappe.db.sql("""
			Select name,first_category
			From `tabItem Second Category` tisc
			Where first_category = '%s'"""%(categories_tuple) ,as_dict=True)

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def third_category_query(doctype, txt, searchfield, start, page_len, filters):
	vritem_code = filters.get('item_code')
	categories = filters.get('categories')
	categories_tuple = tuple(categories)
	if len(categories) != 1:
		return frappe.db.sql("""
			Select name,second_category
			From `tabItem Third Category` tisc
			Where second_category in {}""".format(categories_tuple) ,as_dict=True)
	else:
		return frappe.db.sql("""
			Select name,second_category,first_category
			From `tabItem Third Category` tisc
			Where second_category = '%s'"""%(categories_tuple) ,as_dict=True)

@frappe.whitelist()
def insert_selected_first_category(selected_categories):
	selected_categories = json.loads(selected_categories)
	rows = []
	for category in selected_categories:
		category_doc = frappe.get_doc("Item First Category", category)
		rows.append({
			'first_category': category
		})
	return rows

@frappe.whitelist()
def insert_selected_second_category(selected_categories):
	selected_categories = json.loads(selected_categories)
	rows = []
	for category in selected_categories:
		category_doc = frappe.get_doc("Item Second Category", category)
		rows.append({
			'second_category': category
		})
	return rows

@frappe.whitelist()
def insert_selected_third_category(selected_categories):
	selected_categories = json.loads(selected_categories)
	rows = []
	for category in selected_categories:
		category_doc = frappe.get_doc("Item Third Category", category)
		rows.append({
			'third_category': category
		})
	return rows
