#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 
#######################################################################################
#                             <°))))><
#
#               Script to calculate the actual salary
#
#               by Jens Zorn
#
#
#               - uses the functions provided in 2021
#               - no implementation of Lohnsteuer / Kind etc yet
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
import sys
import config


# things insurance etc.
wage = ""
health_insurance = 0.073
pension_insurance = 0.093
unemployement_insurance = 0.012
nursing_insurance_with_child = 0.01525
nursing_insurance_without_child = 0.01775

def check_wage_option():
    global wage_option
    while True:
        try:
            wage_option = input("Stundenlohn, Bruttolohn oder Jahresbruttolohn? ")
            wage_option = wage_option.lower()
            if wage_option == "stundenlohn":
                return wage_option
            elif wage_option == "bruttolohn":
                return wage_option
            elif wage_option == "jahresbruttolohn":
                return wage_option
            else:
                print("Try again!")
        except:
            print("Try again!")

def check_wage_input():
    global wage
    global wage_option
    global hours
    while True:
        try:
            wage = input("Hier Lohn eingeben: ")
            wage = float(wage)
            if wage_option == "stundenlohn":
                hours = input("Stunden eingeben: ")
                hours = float(hours)
                wage = wage * hours * 4 * 12
                return wage_option, wage
            elif wage_option == "bruttolohn":
                wage = wage * 12
                return wage_option, wage
            elif wage_option == "jahresbruttolohn":
                wage = wage
                return wage_option, wage
            else:
                print("Try again!")
            return wage
        except:
            print("Try again!")

def abzuege():
    global wage
    global pension_insurance
    global unemployement_insurance
    global nursing_insurance_with_child
    global nursing_insurance_without_child
    print("Ihr Jahresgehalt beträgt " + str(wage) + " €")
    health = round(wage * health_insurance, 2)
    pension = round(wage * pension_insurance, 2)
    unemployement = round(wage * unemployement_insurance, 2)
    nursing = round(wage * nursing_insurance_with_child, 2)
    if wage <= 9774:
        wage = round(wage - health - pension - unemployement - nursing, 2)
        tax = 0

    elif 9775 < wage <= 14753:
        y = (wage - 9744) / 10000
        tax = round((995.21 * y + 1400) * y, 2)
        wage = wage - tax - health - pension - unemployement - nursing

    elif 14754 < wage <= 57918:
        y = (wage - 14753) / 10000
        tax = round((208.85 * y + 2397) * y + 950.96, 2)
        wage = wage - tax - health - pension - unemployement - nursing

    elif 57919 < wage <= 274612:
        tax = round(0.42 * wage - 9136.63, 2)
        wage = wage - tax - health - pension - unemployement - nursing

    elif 274613 < wage:
        tax = round(0.45 * wage - 17374.99, 2)
        wage = wage - tax - health - pension - unemployement - nursing

    print("Die Krankenversicherung beträgt: " + str(health) + " €")
    print("Die Rentenversicherung beträgt: " + str(pension) + " €")
    print("Die Arbeitslosenversicherung beträgt: " + str(unemployement) + " €")
    print("Die Pflegeversicherung beträgt: " + str(nursing) + " €")
    print("Die Lohnsteuer beträgt: " + str(tax) + " €")
    print("Dein Nettojahreslohn beträgt: " + str(round(wage, 2)) + " €")
    wage = round(wage / 12, 2)
    print("Dein Nettolohn beträgt: " + str(wage) + " €")

while True:
    check_wage_option()
    check_wage_input()
    abzuege()
    text = input("Weitermachen? (Tippe: 1), oder aufhören? (Tippe: 2) ")
    if text == "2":
        break