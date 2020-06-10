"""
Program : validation_with_try.py
Author : Olivia Kennedy
Date Last Modified : 06/10/2020
This program will accept the input of 3 positive scores and provide an output of the scores.
Bad input (negative numbers) will cause ValueError(s), as well as prompt the user to try again.
"""

#defines average function and creates an exception for bad input
def average(score1, score2, score3):
    try:
        if score1 < 0:
            raise ValueError
        if score2 < 0:
            raise ValueError
        if score3 < 0:
            raise ValueError
    except ValueError:
        print("Please try again and make sure to enter positive numbers for all of the scores to get your average.")
        raise ValueError
    else:
        return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    NUMBER_TESTS = 3
    score1 = float(input("Enter the first score:"))
    score2 = float(input("Enter the second score:"))
    score3 = float(input("Enter the third score:"))
    print("Average Grade:",average(score1, score2, score3), "out of 100")


