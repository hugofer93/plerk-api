#!/usr/bin/python

from csv import reader as csv_reader
from decimal import Decimal
from distutils.util import strtobool
from os import environ
from sys import exit, path

from django import setup as django_setup

path.append('.')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'plerk.settings')

django_setup()

from plerk.apps.companies.models import Company
from plerk.apps.transactions.models import Transaction

rows = list()

with open('utility/test_database.csv', 'r') as file:
    csvreader = csv_reader(file)
    next(csvreader)
    COMPANY_NAME_INDEX = 0
    PRICE_INDEX = 1
    DATE_INDEX = 2
    STATUS_TRANSACTION_INDEX = 3
    STATUS_APPROVED_INDEX = 4

    for row in csvreader:
        # if the company name is empty
        if not row[COMPANY_NAME_INDEX]:
            continue

        valid_status_list = [
            Transaction.CLOSED_STATUS,
            Transaction.REVERSED_STATUS,
            Transaction.PENDING_STATUS,
        ]
        # if there is no valid transaction status
        if row[STATUS_TRANSACTION_INDEX] not in valid_status_list:
            continue

        # Get or create company
        company, _ = Company.objects.get_or_create(
            name=row[COMPANY_NAME_INDEX]
        )

        # Fix the price
        price = row[PRICE_INDEX]
        if len(price.split('.')) == 1:
            price = Decimal(price)
            price = round(price / 100, ndigits=2)

        # Create transaction
        transaction = Transaction(
            company=company,
            price=price,
            date=row[DATE_INDEX],
            status=row[STATUS_TRANSACTION_INDEX],
            status_approved=bool(strtobool(row[STATUS_APPROVED_INDEX])),
            final_payment=False
        )

        # Calculate tax
        transaction.tax_value = Transaction.calculate_tax(transaction.price)

        if transaction.status_approved and transaction.status == 'closed':
            transaction.final_payment = True

        transaction.save()
        print(
            f'Company: {company}'
            f' | Transaction: ${transaction.price}'
            f' | Final Payment: {transaction.final_payment}'
        )

exit()
