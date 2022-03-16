from . import __version__ as app_version

app_name = "masar_oldtimer"
app_title = "Masar Oldtimer"
app_publisher = "KCSC"
app_description = "OldTimer"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@kcsc.com.jo"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_oldtimer/css/masar_oldtimer.css"
# app_include_js = "/assets/masar_oldtimer/js/masar_oldtimer.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_oldtimer/css/masar_oldtimer.css"
# web_include_js = "/assets/masar_oldtimer/js/masar_oldtimer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "masar_oldtimer/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "masar_oldtimer.install.before_install"
# after_install = "masar_oldtimer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_oldtimer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doctype_js = {
    "Item" : "custom/item/item.js",
    "Warehouse" : "custom/warehouse/warehouse.js",

 }
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_oldtimer.tasks.all"
# 	],
# 	"daily": [
# 		"masar_oldtimer.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_oldtimer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_oldtimer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"masar_oldtimer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "masar_oldtimer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "masar_oldtimer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_oldtimer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"masar_oldtimer.auth.validate"
# ]
fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
		"Item-categories",
		# "Item-item_third_category",
		# "Item-item_second_category",
		# "Item-item_first_category",
        "Item-motorcycles",
        "Item-item_motorcycles",
        "Item-item_dimension",
        "Item-item_height",
        "Item-item_length",
        "Item-item_width",
        "Item-volumetric_factor",
        "Item-volumetric_weight",
        "Item-column_break_39",
        "Item-ecommerce",
        "Item-publish_on_oldtimer",
        "Item-publish_on_motosapiens",
        "Item-publish_on_bajadesigns",
        "Item-column_break_44",
        "Item-column_break_46",
        "Warehouse-bin_location",
        "Warehouse-aisle",
        "Warehouse-column_break_2",
        "Warehouse-unit",
        "Warehouse-shelf",
        "Warehouse-shelf_column",
        "Warehouse-bin",
        "Warehouse-column_break_15",
        #"Item Motorcycle-year",
        #"Item Motorcycle-brand",
        #"Item Motorcycle-model",
        "Item-add_third_category",
        "Item-add_second_category",
        "Item-add_first_category",
        "Item-third_category",
        "Item-second_category",
        "Item-first_category",
        "Item-column_break_38",
        "Item-cars",
        "Item-sport_track",
        "Item-off_road",
        "Item-adv_touring",
        "Item-cafe_urban",
        "Item-section_break_30",
        "Item-item_class"
            ]
        ]
    ]}
]
