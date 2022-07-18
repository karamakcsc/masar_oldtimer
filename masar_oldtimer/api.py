import frappe
import requests , json

# @frappe.whitelist()
# def get_item_details(item=None):
# 	return frappe.db.sql(""" SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, ti.publish_on_bajadesigns,
# 								tip.price_list, price_list_rate, tisc.second_category, titc.third_category
# 							FROM `tabItem` ti
# 							inner JOIN `tabItem Price` tip
# 							ON (tip.item_code = ti.item_code AND tip.brand =ti.brand)
# 							LEFT JOIN `tabItem Second Category Value` tisc
# 							ON ti.item_code = tisc.second_category
# 							LEFT JOIN `tabItem Third Category Value` titc
# 							ON ti.item_code = titc.parent
# 							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1 AND tip.price_list = 'BajaDesigns MSRP -USD'
# 							ORDER BY ti.creation DESC;""", as_dict=True)




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


@frappe.whitelist()
def get_item_details(item=None):
	return frappe.db.sql(""" SELECT *
							FROM `tabItem`
							WHERE disabled= 0 AND brand = 'Baja Designs' AND publish_on_bajadesigns = 1
							ORDER BY creation DESC;""", as_dict=True)
