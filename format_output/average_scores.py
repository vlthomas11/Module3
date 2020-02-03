def average(score1,score2, score3):

    scoreA = int(score1)
    scoreB = int(score2)
    scoreC = int(score3)
    avg = (scoreA + scoreB + scoreC)/3

    return avg

# pass

def getting_multiple_inputs():
    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    age = input("What is your age? ")
    score1 = input("what is your first score? ")
    score2 = input("What is your second score? ")
    score3 = input("What is your thrird score? ")
    average_scores = average(score1,score2,score3)
    print(last_name,", ",first_name," age: ",age," average grade: ",average_scores)

if __name__ == '__main__':
    getting_multiple_inputs()