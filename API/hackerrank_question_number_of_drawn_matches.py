import math
import os
import random
import re
import sys
import requests
import json


# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year


def getWinnerTotalGoals(competition, year):

    ### Find Winning Team
    response = requests.get('https://jsonmock.hackerrank.com/api/football_competitions?name='+str(competition)+'&year='+str(year))
    winning_team = response.json()['data'][0]['winner']
    print("Winning Team:" + winning_team)

    goals=0

    for number in range(1,2+1):
        ### Find out how many pages for each url
        response = requests.get('https://jsonmock.hackerrank.com/api/football_matches?competition='+str(competition)+'&year='+str(year)+'&team'+str(number)+'='+str(winning_team))
        total_pages = response.json()['total_pages']
        # print("\nTotal Pages: ", total_pages)
        # Go through all the pages
        for page in range(1,total_pages+1):
            response = requests.get('https://jsonmock.hackerrank.com/api/football_matches?competition='+str(competition)+'&year='+str(year)+'&team'+str(number)+'='+str(winning_team)+'&page='+str(page))
        ### Iterate through data in page, and add up how many goals have been scored
            for data in response.json()['data']:
                # print()
                # print(data)
                goals+=int(data['team'+str(number)+'goals'])
                # print("Goals so far:"+str(goals))

    return goals


if __name__ == '__main__':
    print(getWinnerTotalGoals("English Premier League", 2014))    #Expected output is 73
    # print(getWinnerTotalGoals("La Liga", 2012))                   #Expected output is 115
    # print(getWinnerTotalGoals("UEFA Champions League", 2011))     #Expected output is 28