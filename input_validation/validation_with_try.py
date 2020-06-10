
def average(score1, score2, score3):
    try:
        if score1 < 0:
            raise ValueError
    except ValueError:
        print("Please try again and enter a positive number for score 1 to get your average.")
        raise ValueError
    try:
        if score2 < 0:
            raise ValueError
    except ValueError:
        print("Please try again and enter a positive number for score 2 to get your average.")
        raise ValueError
    else:
        return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    NUMBER_TESTS = 3
    score1 = float(input("Enter the first score:"))
    score2 = float(input("Enter the second score:"))
    score3 = float(input("Enter the third score:"))
    print("Average Grade:",average(score1, score2, score3), "out of 100")


