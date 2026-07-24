# Day 10 - Mini Project: Personal Finance Tracker
# Author: Vishvi
# Date: 2026-07-24
# Uses: OOP, file handling, loops, dicts, error handling

import json, datetime

class Transaction:
    def __init__(self, type_, category, amount, note=''):
        self.type     = type_
        self.category = category
        self.amount   = amount
        self.note     = note
        self.date     = str(datetime.date.today())

    def to_dict(self):
        return {'type': self.type, 'category': self.category,
                'amount': self.amount, 'note': self.note, 'date': self.date}

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.filename     = 'finance.json'
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.transactions, f, indent=4)
        print('Saved!')

    def add(self, type_, category, amount, note=''):
        t = Transaction(type_, category, amount, note)
        self.transactions.append(t.to_dict())
        print(f'Added: {type_} - {category} - Rs{amount}')

    def summary(self):
        income  = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expense = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        print(f'Income: Rs{income} | Expense: Rs{expense} | Balance: Rs{income-expense}')

    def show_all(self):
        if not self.transactions:
            print('No transactions yet!')
            return
        for i, t in enumerate(self.transactions, 1):
            print(f"{i}. {t['date']} | {t['type'].upper()} | {t['category']} | Rs{t['amount']}")

tracker = FinanceTracker()
tracker.add('income',  'salary',    50000)
tracker.add('expense', 'food',       3000)
tracker.add('expense', 'transport',  1500)
tracker.add('income',  'freelance', 10000)
tracker.show_all()
tracker.summary()
tracker.save()
