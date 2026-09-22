import frappe

# `select` grants added to the shipped DocType JSON in this release, so that roles
# which can write a form can also use its link pickers.
#
# A DocType whose permissions have been customised does not read the shipped rows at
# all: get_valid_perms() keeps a shipped DocPerm row only when its parent has no
# Custom DocPerm row, so on those DocTypes the new grants never take effect and the
# pickers stay empty. Mirror them into Custom DocPerm, for those DocTypes only.
#
# DocTypes that have not been customised are deliberately left alone -- they read the
# shipped JSON, they already have these rows, and creating Custom DocPerm rows for
# them would permanently detach them from future permission updates.
GRANTS = {
	"Account": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Manufacturing User",
		"Purchase Master Manager",
		"Quality Manager",
		"Sales Master Manager",
		"Stock Manager",
	],
	"Activity Type": [
		"Accounts User",
		"HR User",
		"Manufacturing User",
	],
	"Asset": [
		"Manufacturing Manager",
		"Manufacturing User",
		"Purchase Manager",
		"Purchase User",
		"Stock Manager",
		"Stock User",
	],
	"Asset Category": [
		"Item Manager",
	],
	"Asset Maintenance Team": [
		"Quality Manager",
	],
	"Asset Shift Factor": [
		"Quality Manager",
	],
	"BOM": [
		"Maintenance User",
		"Purchase Manager",
		"Purchase User",
		"Sales Manager",
		"Sales User",
		"Stock Manager",
		"Stock User",
	],
	"Bank": [
		"Accounts Manager",
		"Accounts User",
	],
	"Bank Account": [
		"Purchase Manager",
		"Purchase Master Manager",
		"Sales Master Manager",
		"Sales User",
	],
	"Batch": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Manufacturing User",
		"Purchase Master Manager",
		"Quality Manager",
		"Sales Manager",
		"Sales Master Manager",
		"Sales User",
	],
	"Blanket Order": [
		"Maintenance Manager",
		"Maintenance User",
		"Purchase Manager",
		"Purchase User",
		"Sales Manager",
		"Sales User",
	],
	"Brand": [
		"Website Manager",
	],
	"Company": [
		"Desk User",
		"Sales Manager",
	],
	"Cost Center": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Manufacturing User",
		"Projects Manager",
		"Projects User",
		"Purchase Master Manager",
		"Quality Manager",
		"Sales Master Manager",
		"Stock Manager",
	],
	"Coupon Code": [
		"Maintenance Manager",
		"Maintenance User",
	],
	"Customer": [
		"Delivery Manager",
		"Delivery User",
		"Employee",
		"Fulfillment User",
		"HR Manager",
		"HR User",
		"Maintenance Manager",
		"Maintenance User",
		"Projects Manager",
		"Projects User",
		"Purchase Master Manager",
		"Quality Manager",
		"Support Team",
		"Website Manager",
	],
	"Customer Group": [
		"Item Manager",
		"Maintenance Manager",
		"Maintenance User",
		"Purchase Manager",
		"Website Manager",
	],
	"Department": [
		"Accounts User",
		"Projects Manager",
		"Projects User",
		"Quality Manager",
	],
	"Driver": [
		"Fulfillment User",
		"Sales User",
		"Stock Manager",
		"Stock User",
	],
	"Employee": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Fleet Manager",
		"Manufacturing Manager",
		"Manufacturing User",
		"Projects User",
		"Quality Manager",
		"Sales Master Manager",
		"Stock Manager",
	],
	"Finance Book": [
		"HR Manager",
		"Manufacturing Manager",
		"Quality Manager",
	],
	"Fiscal Year": [
		"Sales Master Manager",
	],
	"Holiday List": [
		"Accounts Manager",
		"Manufacturing User",
		"Projects Manager",
		"Projects User",
		"Sales Manager",
	],
	"Incoterm": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
	],
	"Issue": [
		"Projects User",
	],
	"Issue Priority": [
		"Support Team",
	],
	"Item Tax Template": [
		"Delivery Manager",
		"Delivery User",
		"Item Manager",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Purchase Manager",
		"Purchase User",
		"Sales Manager",
		"Sales User",
		"Stock Manager",
		"Stock User",
	],
	"Lead": [
		"Support Team",
	],
	"Location": [
		"Quality Manager",
	],
	"Loyalty Program": [
		"Sales Master Manager",
		"Sales User",
	],
	"Manufacturer": [
		"Accounts Manager",
		"Accounts User",
	],
	"Market Segment": [
		"Sales Master Manager",
	],
	"Material Request": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance User",
		"Manufacturing Manager",
	],
	"Mode of Payment": [
		"Maintenance Manager",
		"Maintenance User",
		"Purchase Manager",
		"Purchase User",
		"Sales Manager",
		"Sales User",
	],
	"Monthly Distribution": [
		"Sales Master Manager",
	],
	"POS Invoice": [
		"Sales Manager",
		"Sales User",
	],
	"POS Profile": [
		"Sales Manager",
	],
	"Payment Term": [
		"Maintenance Manager",
		"Maintenance User",
		"Purchase Manager",
		"Purchase User",
		"Sales Manager",
		"Sales User",
	],
	"Plant Floor": [
		"Manufacturing User",
	],
	"Price List": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Stock Manager",
		"Website Manager",
	],
	"Product Bundle": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
	],
	"Project": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Manufacturing User",
		"Purchase Manager",
		"Purchase Master Manager",
		"Purchase User",
		"Quality Manager",
		"Sales Manager",
		"Sales Master Manager",
		"Sales User",
		"Stock Manager",
		"Stock User",
		"Support Team",
	],
	"Project Template": [
		"Projects Manager",
		"Projects User",
	],
	"Purchase Invoice": [
		"Manufacturing Manager",
		"Quality Manager",
		"Stock Manager",
	],
	"Purchase Receipt": [
		"Delivery Manager",
		"Delivery User",
		"Quality Manager",
	],
	"Purchase Taxes and Charges Template": [
		"Accounts Manager",
		"Accounts User",
		"Manufacturing Manager",
		"Stock Manager",
	],
	"Quality Inspection": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Manufacturing Manager",
		"Manufacturing User",
		"Purchase User",
		"Sales User",
		"Stock Manager",
		"Stock User",
	],
	"Sales Forecast": [
		"Stock Manager",
	],
	"Sales Order": [
		"Projects Manager",
		"Projects User",
	],
	"Sales Partner": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Purchase Manager",
		"Stock Manager",
		"Website Manager",
	],
	"Sales Partner Type": [
		"Sales Master Manager",
	],
	"Sales Person": [
		"Accounts Manager",
		"Accounts User",
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Stock Manager",
	],
	"Sales Taxes and Charges Template": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Stock Manager",
	],
	"Serial No": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance User",
		"Quality Manager",
	],
	"Serial and Batch Bundle": [
		"Accounts Manager",
		"Accounts User",
		"Maintenance Manager",
		"Maintenance User",
		"Quality Manager",
	],
	"Shipment Parcel Template": [
		"Stock Manager",
	],
	"Shipping Rule": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Purchase Manager",
		"Purchase User",
		"Stock Manager",
	],
	"Supplier": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance User",
		"Quality Manager",
		"Sales Master Manager",
		"Website Manager",
	],
	"Supplier Group": [
		"Sales Manager",
		"Website Manager",
	],
	"Supplier Quotation": [
		"Maintenance Manager",
		"Maintenance User",
	],
	"Task": [
		"Accounts User",
		"Employee",
		"Manufacturing User",
	],
	"Tax Category": [
		"Delivery Manager",
		"Delivery User",
		"Item Manager",
		"Maintenance Manager",
		"Maintenance User",
		"Manufacturing Manager",
		"Purchase Manager",
		"Purchase Master Manager",
		"Purchase User",
		"Sales Manager",
		"Sales Master Manager",
		"Sales User",
		"Stock Manager",
		"Stock User",
	],
	"Tax Withholding Category": [
		"Item Manager",
		"Purchase Manager",
		"Purchase Master Manager",
		"Sales Master Manager",
		"Sales User",
	],
	"Tax Withholding Group": [
		"Accounts Manager",
		"Accounts User",
		"Purchase Manager",
		"Purchase Master Manager",
		"Sales Master Manager",
		"Sales User",
	],
	"Terms and Conditions": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Maintenance User",
	],
	"Territory": [
		"Delivery Manager",
		"Delivery User",
		"Maintenance Manager",
		"Website Manager",
	],
	"UOM": [
		"Desk User",
	],
	"Vehicle": [
		"Fulfillment User",
		"Stock User",
	],
	"Warehouse": [
		"Delivery Manager",
		"Delivery User",
		"HR Manager",
		"Maintenance Manager",
		"Maintenance User",
		"Quality Manager",
		"Website Manager",
	],
}


# This is the version-15 shape of the patch, and it is deliberately NOT the one that runs on
# version-16. The v16 patch carries a third clause that skips a pair when a `Permission Log`
# row records it as deliberately removed. That DocType does not exist on frappe v15 at all, and
# `frappe.get_all` on a missing DocType raises DoesNotExistError outside the savepoint, which
# would abort `migrate` on the first customised DocType. So the predicate here is two-way.
#
# Dropping the third clause is safe here because of a measurement, not convenience: none of the
# pairs below ever shipped a DocPerm row before this release, so `copy_perms` could never have
# produced one, so the pair was never visible in Role Permission Manager for an administrator to
# remove. There is nothing for a third clause to catch.
#
# `Deleted Document` is not a substitute. It records every delete_doc, but it is purged by
# clear_old_logs(days=180), so a site past its retention window reads as never-existed and the
# clause would fail OPEN -- granting back a row an administrator had deliberately removed.
#
# The patch therefore carries its own name, distinct from the v16 one, so that if `Permission
# Log` is ever backported the v16 patch is still free to run here. A name burned in `Patch Log`
# never gets a second chance.

# Most pairs below are mirrored as `select` and nothing else, matching the shipped row they
# stand in for. These are the exceptions: their shipped rows grant more than `select`, so a
# select-only mirror would not match. It would also BREAK the form -- `select` does not imply
# `read` on this branch (there is no fallback in either direction here), and
# bom.get_bom_items() checks `read`. Each entry is the exact ptype set of the shipped row.
PAIR_PTYPES = {
	("BOM", "Purchase Manager"): ("read", "select"),
	("BOM", "Purchase User"): ("read", "select"),
	("BOM", "Stock Manager"): ("read", "select"),
	("BOM", "Stock User"): ("read", "select"),
	("Company", "Sales Manager"): ("read",),
	("Material Request", "Manufacturing Manager"): ("read", "report"),
}

# Custom DocPerm defaults `read` and `export` to 1, and frappe.permissions.add_permission
# leaves those defaults in place, so every ptype is written explicitly here: a row gets exactly
# the ptypes its shipped counterpart has and nothing else.
PTYPES = (
	"read",
	"write",
	"create",
	"delete",
	"submit",
	"cancel",
	"amend",
	"report",
	"export",
	"import",
	"share",
	"print",
	"email",
)

SAVEPOINT = "mirror_select_perms_to_custom_docperm_two_way"


def execute():
	for doctype, roles in GRANTS.items():
		if not frappe.db.exists("DocType", doctype):
			continue

		# clause 1: only DocTypes already carrying Custom DocPerm rows
		if not frappe.db.exists("Custom DocPerm", {"parent": doctype}):
			continue

		added = False

		for role in roles:
			if not frappe.db.exists("Role", role):
				continue

			# clause 2: leave any existing rule for this role and level as the site
			# configured it, whatever its ptypes
			if frappe.db.exists("Custom DocPerm", {"parent": doctype, "role": role, "permlevel": 0}):
				continue

			try:
				frappe.db.savepoint(SAVEPOINT)

				row = frappe.new_doc("Custom DocPerm")
				granted = PAIR_PTYPES.get((doctype, role), ("select",))
				row.update(
					{
						"parent": doctype,
						"parenttype": "DocType",
						"parentfield": "permissions",
						"role": role,
						"permlevel": 0,
						"if_owner": 0,
					}
				)
				# PTYPES is the clearing list and deliberately excludes `select`; write that too,
				# otherwise a pair whose granted set includes it silently gets read-only
				for ptype in (*PTYPES, "select"):
					row.set(ptype, 1 if ptype in granted else 0)

				row.insert(ignore_permissions=True)
				added = True
			except Exception:
				# Roll back before logging. A failed statement leaves the transaction
				# unusable on Postgres, so log_error() would fail too and the migration
				# would stop with only part of the rows written.
				frappe.db.rollback(save_point=SAVEPOINT)
				frappe.log_error(
					title="Could not add select permission",
					message=f"{doctype} / {role}\n\n{frappe.get_traceback()}",
				)

		if added:
			frappe.clear_cache(doctype=doctype)
