import csv
import time


def getscore(username):
    file = open('UserReport.csv')
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == username:
            creditscore = int(row[3])
            return(creditscore)
            break

def creditadvice(username):
    credit = getscore(username)
    if credit >= 750:
        print('Your credit score looks good.\n')

    elif credit >= 650 and credit < 750: 
        print('Your credit score could be improved.\nHere are some tips:\n')
        print('• Register to vote')
        print('• Check your Utility Provider to compare quotes')
        print('• Pay credit card balances strategically\n')
    
    else:
        print('Your credit score is low and needs improvement.\nHere are some tips:')
        print('• Register to vote')
        print('• Check your Utility Provider to compare quotes')
        print('• Pay credit card balances strategically')
        print('• Ask for a higher credit limit')
        print('• Pay bills on time')
        print('• Use a secure credit card\n')


def gethousing(username):
    file = open('UserReport.csv')
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == username:
            housingscore = int(row[8])
            return(housingscore)
            break

def housingadvice(username):
    housing = gethousing(username) / getincome(username)

    if housing >= 25 and housing <= 35:
        print('You are spending the average amount on housing\n')

    elif housing < 25:
        print('You are spending less than the average on housing.\n')

    else:
        ('You are spending more than the average on housing. It may be advisable to optimise housing spending.\n')


def getTransport(username):
    file = open('UserReport.csv')
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == username:
            TransportScore = int(row[9])
            return(TransportScore)
            break

def transportAdvice(username):
    transport = getTransport(username) / getincome(username)
    if transport>=10 and transport<=15:
        print("You are spending the average amount on transportation.\n")
    elif transport<=10:
        print("You are saving money on transportation.\n")
    else:
        print("You are using more than the average on transportation. It may be advisable to spend less\n")


def getEntertainment(username):
    file = open('UserReport.csv')
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == username:
            entertainmentScore = int(row[6])
            return(entertainmentScore)
            break

def entertainmentAdvice(username):
    entertainment = getEntertainment(username) / getincome(username)
    if entertainment>=10 and entertainment<=15:
        print("You are using a the resommended amount on recreation and entertainment.\n")
    elif entertainment<=10:
        print("You are saving on recreation and entertainment.\n")
    else:
        print("You are using more than average on recreation and entertainment. We would recommend trying to same more here.\n")


def getincome(username):
    file = open('UserReport.csv')
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == username:
            income = float(row[15])
            return(income)
            break


username = input('please enter username: ')
print('What service would you like to use?\n')
print('1 - Credit Score Advice\n2 - Housing Advice\n3 - Transport Advice\n4 - Entertainment Advice\n')
service = input('Enter number for service: ')
if service == '1':
    getscore(username)
    creditadvice(username)
elif service == '2':
    gethousing(username)
    housingadvice(username)

elif service == '3':
    getTransport(username)
    transportAdvice(username)

elif service == '4':
    getEntertainment(username)
    entertainmentAdvice(username)