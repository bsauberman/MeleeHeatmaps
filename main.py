import copy
#(Left_X, Right_X, Top_Y, Bottom_Y, X_Size, Y_Size)
stageShift = {0: (-175, 173, 168, -91, 349, 259),
              1: (-198, 198, 202, -146, 396, 348),
              2: (-255, 255, 250, -123, 510, 373),
              3: (-230, 230, 180, -111, 460, 291),
              4: (-224, 224, 200, -108, 448, 308),
              5: (-246, 246, 188, -140, 492, 328)}

data = []
for characters in range(7):
  charactersArr = []
  for stages in range(6):
    stagesArr = [[0 for _ in range (stageShift.get(stages)[4])] for _ in range (stageShift.get(stages)[5])]
    charactersArr.append(stagesArr)

  data.append(charactersArr)


chars = {'FOX': 0, 'MARTH': 1, 'JIGGLYPUFF': 2, 'FALCO': 3, 'SHEIK': 4, 'CAPTAIN FALCON': 5, 'PEACH': 6}
stages = {'YOSHIS STORY': 0, 'FOUNTAIN OF DREAMS': 1, 'DREAM LAND N64': 2, 'POKEMON STADIUM': 3, 'BATTLEFIELD': 4, 'FINAL DESTINATION': 5}
#dir = '/content/drive/MyDrive/2021-10/'
dir = 'D:/bsaub/Slippi Files/2021-12/'
pathNames = []


# f = '/content/drive/MyDrive/2021-10/Game_20211031T235224.slp'

import pandas as pd
import slippi as slp
import os

f = ''
count = 0
me = 0
opp = 0
for path in os.listdir(dir):
    if path.endswith("slp") and count < 5:
        print('\nCount: '+ str(count) + " " + path)
        f = dir + path
        game = slp.Game(f)
        # print(game.metadata)
        stage = str(game.start.stage).replace('Stage.', '').replace('_', ' ')
        # print(stages.get(stage))
        if game.metadata.players[0] != None and game.metadata.players[0].netplay != None:
            if game.metadata.players[0].netplay.name == 'Subey':
                me = 0
                opp = 1
            elif game.metadata.players[1].netplay.name == 'Subey':
                me = 1
                opp = 0
            else:
                print(game.metadata.players[0].netplay.name)
                print(game.metadata.players[1].netplay.name)
                continue
        else:
            print('continue2')
            continue
        if me == 0 and opp == 0:
            print('UH OH')
        myChar = str(game.start.players[me].character).replace('CSSCharacter.', '').replace('_', ' ')
        oppChar = str(game.start.players[opp].character).replace('CSSCharacter.', '').replace('_', ' ')

        if myChar != 'MARTH':
            print('I am playing ' + myChar + " apparently...")

        print(myChar + " vs. " + oppChar + " on " + stage)

        stageNum = stages.get(stage)
        oppCharNum = chars.get(oppChar)

        for i in range(123, len(game.frames)):
            frame = game.frames[i].index
            # if frame < 1:
            myLoc = game.frames[i].ports[0].leader.pre.position
            # print(game.frames[i].ports[1].leader.pre.position)


            # print(str(stageNum) + " " + str(oppCharNum))
            if oppCharNum != None and stageNum != None:
                #data[oppCharNum][stageNum].append(myLoc)
                x, y = str(myLoc).replace('(', '').replace(')', '').split(",")
                x = int(float(x)) - stageShift.get(stageNum)[0]
                y = int(float(y)) - stageShift.get(stageNum)[3]
                #print(str(x) + " " + str(y))
                #convertedLoc = [x, y]
                try:
                    if data[oppCharNum][stageNum][y][x]:
                        data[oppCharNum][stageNum][y][x] = data[oppCharNum][stageNum][y][x] + 1
                except IndexError:
                    try:
                        data[oppCharNum][stageNum][y-1][x] += 1
                    except IndexError:
                        try:
                            data[oppCharNum][stageNum][y][x-1] += 1
                        except: pass
                else:
                    pass

        count += 1

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LogNorm, Normalize

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


for c in range(len(data)):
    currChar = get_keys_from_value(chars, c)[0]
    for s in range(len(data[0])):
        min = min([min(r) for r in data[c][s]])
        max = max([max(r) for r in data[c][s]])
        if min != 0 or max != 0:
            currStage = get_keys_from_value(stages, s)[0]
            ax = sns.heatmap(data[c][s], norm = LogNorm(), vmin = min, vmax = max)
            ax.invert_yaxis()
            title = str(str(currChar) + ": " + currStage)
            plt.title(title)
            plt.show()



