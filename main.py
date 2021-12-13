data = []
for i in range(7):
  stageArray = []
  for j in range(6):
    stageArray.append([])
  data.append(stageArray)
print(data)
chars = {'FOX': 0, 'MARTH': 1, 'JIGGLYPUFF': 2, 'FALCO': 3, 'SHEIK': 4, 'CAPTAIN FALCON': 5, 'PEACH': 6}
stages = {'YOSHIS STORY': 0, 'FOUNTAIN OF DREAMS': 1, 'DREAM LAND N64': 2, 'POKEMON STADIUM': 3, 'BATTLEFIELD': 4, 'FINAL DESTINATION': 5}
dir = '/content/drive/MyDrive/2021-10/'
pathNames = []

# f = '/content/drive/MyDrive/2021-10/Game_20211031T235224.slp'

import pandas as pd
import slippi as slp
import os

f = ''
count = 0
for path in os.listdir(dir):
    if path.endswith("slp") and count < 5:
        print(path)
        f = dir + path
        game = slp.Game(f)
        # print(game.metadata)
        stage = str(game.start.stage).replace('Stage.', '').replace('_', ' ')
        # print(stages.get(stage))
        p1 = str(game.start.players[0].character).replace('CSSCharacter.', '').replace('_', ' ')
        p2 = str(game.start.players[1].character).replace('CSSCharacter.', '').replace('_', ' ')
        me = 1
        opp = 2
        if p1 != 'MARTH':
            if p2 == 'MARTH':
                # print('P2')
                me = 2
                opp = 1
            else:
                pass
                # print('Marthless')
        else:
            if p2 != ('MARTH'):
                pass
                # print('P1')
            else:
                # print('Ditto')
                # print(game.metadata)
                if game.metadata.players[1].netplay.name == 'SUBEY':
                    me = 2
                    opp = 1

        print(p1 + " vs. " + p2 + " on " + stage)

        for i in range(123, len(game.frames)):
            frame = game.frames[i].index
            # if frame < 1:
            myLoc = game.frames[i].ports[0].leader.pre.position
            # print(game.frames[i].ports[1].leader.pre.position)

            stageNum = stages.get(stage)
            oppCharNum = chars.get(eval(str('p' + str(opp))))
            # print(str(stageNum) + " " + str(oppCharNum))
            if oppCharNum != None and stageNum != None:
                data[oppCharNum][stageNum].append(myLoc)

        count += 1

print(data)
