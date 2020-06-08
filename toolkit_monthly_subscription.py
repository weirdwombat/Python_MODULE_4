"""
Program : toolkit_monthly_subscription.py
Author : Olivia Kennedy
Date Last Modified : 06/08/2020
This program will accept the input of one of the 5 Programmer's Toolkit Monthly membership
levels and print the cost. If bad input is entered, it will ask the user to try again and enter a valid
option.
"""
#definition for membership
def membership():
    membership = input("Enter your subscription level of choice - Platinum, Gold, Silver, Bronze, or Free Trial:")

    #expected output for input of Platinum is 'Platinum is 60 USD'
    #actual output for user input of 'Platinum' is 'Platinum is 60 USD'
    if (membership == 'Platinum') :
        print('Platinum is 60 USD')

    #expected output for input of Gold is 'Gold is 50 USD'
    #actual output fou user input of 'Gold' is 'Gold is 50 USD'
    elif (membership == 'Gold') :
        print('Gold is 50 USD')

    #expected output for input of Silver is 'Silver is 40 USD'
    #actual output for user input of 'Silver' is 'Silver is 40 USD'
    elif (membership == 'Silver') :
        print('Silver is 40 USD')

    #expected output for input of Bronze is 'Bronze is 30 USD'
    #actual output for user input of 'Bronze' is 'Bronze is 30 USD'
    elif (membership == 'Bronze') :
        print('Bronze is 30 USD')

    #expected output for input of Free Trial is 'The free trial is 0 USD until its expiration'
    #actual output for user input of 'Free Trial' is 'The free trial is 0 USD until its expiration'
    elif (membership == 'Free Trial'):
        print('The free trial is 0 USD until its expiration')

    #bad input will fall under the else condition
    #actual output for bad user input is 'Please try again and enter a valid option'
    else :
        print("Please try again and enter a valid option")

if __name__ == "__main__":
    membership()
