# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:40:17 2020

@author: mfl
"""

import random
import pandas as pd
import pickle

# =============================================================================
# Settings
# =============================================================================

# Rounds in regular season
runder = 14

# Division sizes
division_size = 4

# Team names
team_names = ["Glenny", "Theis", "Hygge", "Magnus", "Mathias", "Jens", 
              "Malthe", "Joachim", "Patrick", "Ahle", "Balder", "Bang"]


# =============================================================================
# Random draw of groups
# =============================================================================

random.shuffle(team_names)

teams = [[team_names[i], i//division_size+1] for i in range(len(team_names))]

print([[j, {i[0] for i in teams if i[1] == j}] for j in range(1,4)])

# teams2 = [["Glenny", 1], ["Theis", 1], ["Hygge", 1], 
#           ["Magnus", 2], ["Mathias", 2], ["Jens", 2], 
#           ["Malthe", 3], ["Joachim", 3], ["Patrick", 3], 
#           ["Ahle", 1], ["Balder", 2], ["Bang", 3]]


# =============================================================================
# Creating random schedule
# =============================================================================

runde_dict = {}

round_count = 0

while (len(runde_dict.keys()) == 0) | any(len(runde_dict[a])!=6 for a in runde_dict):

    league_dict = {}    
    
    teams_copy = teams[:]
    
    team_names = []
    
    for t in teams:
        team_names.append(t[0])
        teams_copy.remove(t)
        team_schedule = [i[0] for i in teams_copy[:]] + [j[0] for j in teams_copy[:] if j[1] == t[1]]
    
        # for t2 in teams_copy:
        #     if t2[1] == t[1]:
        #         team_schedule.append(t2)
        random.shuffle(team_schedule)
        league_dict[t[0]] = team_schedule
    
    for i in range(0,runder):
        if i < 10:
            runde_nr = "0" + str(i)
        else:
            runde_nr = str(i)
        runde_dict["Runde " + runde_nr] = []

    for n in team_names:
        add_team_schedule = league_dict[n][:]
        for i in add_team_schedule:
            for r in runde_dict:
                add = 1
                for k in runde_dict[r]:
                    if (i in k) | (n in k):
                        add = 0
                        break
                if add == 1:
                    runde_dict[r].append([n, i])
                    # print(n, i)
                    break
    round_count += 1

schedule_data = pd.DataFrame(runde_dict)

print(round_count)

# =============================================================================
# Testing
# =============================================================================

teams_copy = teams[:]
team_schedule = []
for t in teams:
    teams_copy.remove(t)
    team_schedule += [[t[0], i[0]] for i in teams_copy[:]]

counter = [0 for j in range(0, runder)]

for i in team_schedule:
    count_team = 0
    count_round = 0
    for j in runde_dict:
        if (i in runde_dict[j]) & (count_team == 1):
            counter[count_round] += 1
            print(j, i)
        elif (i in runde_dict[j]):
            count_team = 1
        count_round += 1
     
print(schedule_data)

# =============================================================================
# Printing schedule
# =============================================================================

schedule_data.to_excel("/Users/malthefaberlaursen/Dropbox/NFL/Fantasy/fantasy-scheduler/schedule_data.xlsx")

# with open("/Users/malthefaberlaursen/Dropbox/NFL/Fantasy/fantasy-scheduler/schedule_data.dat", "wb") as f:
#     pickle.dump(schedule_data, f)
    
# =============================================================================
# Setting schedule on fantasy.nfl.com
# =============================================================================

# email_ = "test"
# password_ = "test"
# fantasy_id_= "3406380"

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import numpy as np

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://fantasy.nfl.com/")

# WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@aria-label="ACCEPTER"]'))
# driver.find_element_by_xpath('//*[@aria-label="ACCEPTER"]').click()

# time.sleep(np.random.uniform(2,5))

# WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_class_name("nav-item"))
# sign_in = driver.find_elements_by_class_name("nav-item")
# for i in sign_in:
#     print(i.text)
#     if i.text == "SIGN IN":
#         i.click()
#         break
    
# time.sleep(np.random.uniform(2,5))

# WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@placeholder="Email or Username *"]'))
# email = driver.find_element_by_xpath('//*[@placeholder="Email or Username *"]')
# email.send_keys(email_)
# password = driver.find_element_by_xpath('//*[@placeholder="Password *"]')
# password.send_keys(password_)
# password.send_keys(webdriver.common.keys.Keys.ENTER)

# time.sleep(np.random.uniform(2,5))

# driver.get("https://fantasy.nfl.com/league/" + fantasy_id_ + "/manage/customscheduleview")










