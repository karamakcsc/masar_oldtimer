import frappe

@frappe.whitelist()
def get_item_details(item=None):
	return frappe.db.sql(""" SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, ti.publish_on_bajadesigns, tip.price_list, price_list_rate
							FROM `tabItem` ti
							inner JOIN `tabItem Price` tip
							ON (tip.item_code = ti.item_code AND tip.brand =ti.brand)
							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1 AND tip.price_list = 'BajaDesigns MSRP -USD'
							ORDER BY ti.creation DESC LIMIT 12;""", as_dict=True)
