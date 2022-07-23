# # from __future__ import unicode_literals
# import frappe, erpnext, json
# from frappe import _, scrub, ValidationError
# from frappe.utils import flt, comma_or, nowdate, getdate
# from erpnext.setup.utils import get_exchange_rate
# from erpnext.accounts.general_ledger import make_gl_entries
# from erpnext.controllers.accounts_controller import AccountsController
# from frappe.model.document import Document
#
#
# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def get_bin_qry(doctype, txt, searchfield, start, page_len, filters):
#     vr_item_code = filters.get('item_code')
#     return frappe.db.sql("""
#         Select name,warehouse,item_code,actual_qty
#         From `tabBin` tb
#         Where actual_qty > 0 and item_code = '%s'"""%(vr_item_code) ,as_dict=True)
#
#
# @frappe.whitelist()
# def insert_selected_bins(selected_bins):
#     selected_bins = json.loads(selected_bins)
#     rows = []
#     for bin_name in selected_bins:
#         bin_doc = frappe.get_doc("Bin", bin_name)
#         rows.append({
#             'item_code': bin_doc.item_code,
#             'warehouse': bin_doc.warehouse
#         })
#     return rows
