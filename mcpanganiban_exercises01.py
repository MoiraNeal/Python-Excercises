""" The Challenge
Author: Moira
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""
bill = float(input('How much is your bill?'))
payment = float(input('How much did you pay?'))
print('Hi! Your change is {}'.format(payment- bill))
