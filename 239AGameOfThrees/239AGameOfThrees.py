#https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/
def threesGame(num):
    while num != 1:
        print num
        if num%3 == 0: 
            num = num / 3
        elif num%3 == 1:
            num = (num - 1) / 3
        elif num%3 == 2:
            num = (num + 1) / 3
    print 1
threesGame(31337357)