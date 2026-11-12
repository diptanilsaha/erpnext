# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

from unittest.mock import patch

import frappe

from erpnext.accounts.doctype.account_closing_balance.account_closing_balance import make_closing_entries
from erpnext.tests.utils import ERPNextTestSuite


def entry(**overrides):
	row = {"debit": 0, "credit": 0, "debit_in_account_currency": 0, "credit_in_account_currency": 0}
	row.update(overrides)
	return row


class TestAccountClosingBalance(ERPNextTestSuite):
	def test_closing_entries_are_bulk_inserted(self):
		# a PCV can make one row per dimension combination; one write per row
		# breaks the write limit of the transaction
		writes_before = frappe.db.transaction_writes
		make_test_closing_entries(500)

		self.assertLess(frappe.db.transaction_writes - writes_before, 5)
		rows = get_test_closing_balances()
		self.assertEqual(len(rows), 500)
		self.assertTrue(all(row.debit == 10 and row.docstatus == 1 for row in rows))
		self.assertEqual({str(row.closing_date) for row in rows}, {"1990-12-31"})

	def test_reporting_currency_rate_is_fetched_once(self):
		company = "_Test Company"
		frappe.db.set_value("Company", company, "reporting_currency", "USD")
		frappe.clear_document_cache("Company", company)
		self.addCleanup(frappe.clear_document_cache, "Company", company)

		module = "erpnext.accounts.doctype.account_closing_balance.account_closing_balance"
		with patch(f"{module}.get_exchange_rate", return_value=2) as get_exchange_rate:
			make_test_closing_entries(3)

		get_exchange_rate.assert_called_once()
		rows = get_test_closing_balances()
		self.assertEqual(len(rows), 3)
		for row in rows:
			self.assertEqual(row.reporting_currency_exchange_rate, 2)
			self.assertEqual(row.debit_in_reporting_currency, 20)
			self.assertEqual(row.credit_in_reporting_currency, 0)

	def test_reporting_amount_of_carried_balance_keeps_its_rate(self):
		module = "erpnext.accounts.doctype.account_closing_balance.account_closing_balance"
		previous = entry(
			company="_Test Company",
			account="Sales - _TC",
			credit=1000,
			credit_in_account_currency=1000,
			credit_in_reporting_currency=12,
		)
		current = frappe._dict(
			entry(company="_Test Company", account="Sales - _TC", credit=500, credit_in_account_currency=500)
		)

		with (
			patch(f"{module}.get_previous_closing_entries", return_value=[previous]),
			patch(f"{module}.get_reporting_currency_exchange_rate", return_value=0.01),
		):
			make_closing_entries([current], "ACB-TEST-PCV", "_Test Company", "2025-05-31")

		self.assertEqual(
			frappe.db.get_value(
				"Account Closing Balance",
				{"period_closing_voucher": "ACB-TEST-PCV"},
				["credit", "credit_in_reporting_currency"],
			),
			(1500, 17),
		)

	def test_carried_balance_is_restated_when_reporting_currency_changes(self):
		company = "_Test Company"
		frappe.db.set_value("Company", company, "reporting_currency", "USD")
		frappe.clear_document_cache("Company", company)
		self.addCleanup(frappe.clear_document_cache, "Company", company)

		module = "erpnext.accounts.doctype.account_closing_balance.account_closing_balance"
		previous = entry(
			company=company,
			account="Sales - _TC",
			closing_date="2025-04-30",
			credit=1000,
			credit_in_account_currency=1000,
			credit_in_reporting_currency=1000,
			reporting_currency="INR",
		)
		current = entry(company=company, account="Sales - _TC", credit=500, credit_in_account_currency=500)
		rates = {"2025-04-30": 0.012, "2025-05-31": 0.01}

		with (
			patch(f"{module}.get_previous_closing_entries", return_value=[previous]),
			patch(f"{module}.get_reporting_currency_exchange_rate", side_effect=lambda _, date: rates[date]),
		):
			make_closing_entries([current], "ACB-TEST-PCV", company, "2025-05-31")

		self.assertEqual(
			frappe.db.get_value(
				"Account Closing Balance",
				{"period_closing_voucher": "ACB-TEST-PCV"},
				["credit", "credit_in_reporting_currency", "reporting_currency"],
			),
			(1500, 17, "USD"),
		)


def make_test_closing_entries(count):
	closing_entries = [
		entry(
			company="_Test Company",
			account="_Test Bank - _TC",
			project=f"_Test Dimension Value {i}",
			debit=10,
			debit_in_account_currency=10,
		)
		for i in range(count)
	]
	make_closing_entries(closing_entries, "_Test Closing Voucher", "_Test Company", "1990-12-31")


def get_test_closing_balances():
	return frappe.get_all(
		"Account Closing Balance",
		filters={"period_closing_voucher": "_Test Closing Voucher"},
		fields=[
			"debit",
			"docstatus",
			"closing_date",
			"reporting_currency_exchange_rate",
			"debit_in_reporting_currency",
			"credit_in_reporting_currency",
		],
	)
