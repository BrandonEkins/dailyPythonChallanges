#https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/?utm_content=title&utm_medium=hot&utm_source=reddit&utm_name=dailyprogrammer

file = open('rabbits.txt', "r")
lines = file.readline().split(" ")
male_rabbits = [lines[0],lines[0],lines[0]]
female_rabbits = [lines[1],lines[1],lines[1]]
rabbits_needed_alive = lines[2]
time = 2

while sum(male_rabbits[-96:]) + sum(female_rabbits[:-96]) < rabbits_needed_alive: 
    if (time - 4) >=0:
        male_rabbits.append(sum(female_rabbits[(time-96):-4])*5)
        femalie_rabbits.append(sum(femal_rabbits[(time-96):-4])*9)
    time = len(male_rabbits-1)        

print time
