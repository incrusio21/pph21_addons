from . import __version__ as app_version

app_name = "pph21_addons"
app_title = "PPH21 TER ADDONS"
app_publisher = "DAS"
app_description = "PPH21 TER ADDONS"
app_email = "das@das.com"
app_license = "MIT"
fixtures = [ 
	{
		"dt": "PPh21 TER Master",
		"filters":[["name", "in", ['TER A', 'TER B', 'TER C']]]
	},
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pph21_addons/css/pph21_addons.css"
# app_include_js = "/assets/pph21_addons/js/pph21_addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/pph21_addons/css/pph21_addons.css"
# web_include_js = "/assets/pph21_addons/js/pph21_addons.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pph21_addons/public/scss/website"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "pph21_addons.utils.jinja_methods",
#	"filters": "pph21_addons.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pph21_addons.install.before_install"
# after_install = "pph21_addons.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pph21_addons.uninstall.before_uninstall"
# after_uninstall = "pph21_addons.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pph21_addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
    "Salary Slip": {
        "validate": "pph21_addons.doctype_function.pph21_core.calculate_tax"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"pph21_addons.tasks.all"
#	],
#	"daily": [
#		"pph21_addons.tasks.daily"
#	],
#	"hourly": [
#		"pph21_addons.tasks.hourly"
#	],
#	"weekly": [
#		"pph21_addons.tasks.weekly"
#	],
#	"monthly": [
#		"pph21_addons.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "pph21_addons.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "pph21_addons.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "pph21_addons.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pph21_addons.utils.before_request"]
# after_request = ["pph21_addons.utils.after_request"]

# Job Events
# ----------
# before_job = ["pph21_addons.utils.before_job"]
# after_job = ["pph21_addons.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"pph21_addons.auth.validate"
# ]
