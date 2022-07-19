import frappe
import requests , json


@frappe.whitelist()
def get_item_details(item=None):
	return frappe.db.sql(""" SELECT * ,tifcv.first_category, tiscv.second_category, titcv.third_category, tip.price_list_rate, tf.file_url, tim.motorcycle
							FROM `tabItem` ti
							LEFT Join `tabFile` tf
							ON ti.item_code = tf.attached_to_name
							LEFT JOIN `tabItem First Category Value` tifcv
							ON tifcv.parent = ti.item_code
							LEFT JOIN `tabItem Second Category Value` tiscv
							ON tiscv.parent = ti.item_code
							LEFT JOIN `tabItem Third Category Value` titcv
							ON titcv.parent = ti.item_code
							LEFT JOIN `tabItem Price` tip
							ON tip.item_code = ti.item_code
							LEFT JOIN `tabItem Motorcycle` tim
							ON tip.parent = ti.item_code
							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1 AND tip.price_list = 'BajaDesigns MSRP -USD'
							ORDER BY ti.creation DESC;""", as_dict=True)

# @frappe.whitelist()
# def get_item_details(item=None):
# 	return frappe.db.sql(""" SELECT ti.name, ti.item_name, ti.item_code, ti.description, ti.image, ti.disabled, ti.variant_of, ti.publish_on_bajadesigns, tf.file_url
# 							FROM `tabItem` ti
# 							Inner Join `tabFile` tf
# 							ON ti.item_code = tf.attached_to_name
# 							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1
# 							GROUP BY ti.item_code ORDER BY ti.creation DESC;""", as_dict=True)


@frappe.whitelist()
def get_variants_details(variant=None):
	return frappe.db.sql(""" SELECT *, tf.file_url
							FROM `tabItem` ti
							Inner Join `tabFile` tf
							ON ti.item_code = tf.attached_to_name
							WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1 AND ti.variant_of <> ""
							GROUP BY ti.item_code ORDER BY ti.creation DESC;""", as_dict=True)




@frappe.whitelist()
def get_cat(cat_nd=None):
	return frappe.db.sql(""" SELECT ti.item_code, tiscv.second_category, titcv.third_category
								FROM `tabItem` ti
								INNER JOIN `tabItem Second Category Value` tiscv
								ON tiscv.parent = ti.item_code
								INNER JOIN `tabItem Third Category Value` titcv
								ON titcv.parent = ti.item_code
								WHERE ti.disabled= 0 AND ti.brand = 'Baja Designs' AND ti.publish_on_bajadesigns = 1
								GROUP BY ti.item_code  ORDER BY ti.creation DESC;""", as_dict=True)

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
