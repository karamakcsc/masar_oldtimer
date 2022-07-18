import frappe
import requests , json

@frappe.whitelist()
def get_item_details(item=None):
	return frappe.db.sql(""" SELECT * ,tf.file_url
							FROM `tabItem` ti
							Inner Join `tabFile` tf
							ON ti.item_code = tf.attached_to_name
							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1
							ORDER BY ti.creation DESC;""", as_dict=True)


@frappe.whitelist()
def get_variants_details(variant=None):
	return frappe.db.sql(""" SELECT *, tf.file_url
							FROM `tabItem` ti
							Inner Join `tabFile` tf
							ON ti.item_code = tf.attached_to_name
							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1 AND ti.variant_of <> ""
							GROUP BY ti.item_code ORDER BY ti.creation DESC;""", as_dict=True)




# @frappe.whitelist()
# def get_second_cat(cat_nd=None):
# 	return frappe.db.sql(""" SELECT name, creation, first_category, second_category
# 						   FROM `tabItem Second Category`  WHERE first_category ='Cars' ORDER BY creation DESC ;""", as_dict=True)

# @frappe.whitelist()
# def get_item_filter(item=None):
# 		return frappe.db.sql(""" SELECT parent, third_category
# 							FROM `tabItem Third Category Value`
#
# 							ORDER BY creation DESC limit 0, 50;""", as_dict=True)
#
#
#
# @frappe.whitelist()
# def get_item_filters(item=None):
# 		items = frappe.db.sql("""select c.item_code, i.third_category from `tabItem` as c left join `tabItem Third Category Value` as i on c.item_code =i.parent
# 										 ORDER BY i.creation DESC ;""", as_dict=True)
# 		return items
