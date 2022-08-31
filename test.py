import random

def Team_Generator():

    num_teams = int(input("How many teams? : "))
    with open('class_list.txt', "r") as readfile: 
        people = readfile.readlines()

    num_people = len(people)

    while num_people > 0 and num_teams > 0:
            
        team = random.sample(people, int(num_people/num_teams))

        for x in team:
            people.remove(x)
        
        num_people-=int(num_people/num_teams)
        num_teams-=1
        print(team)

Team_Generator()
