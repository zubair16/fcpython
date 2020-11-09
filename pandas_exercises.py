import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PlayerList = ["Pagbo","Grazemen","Cantay","Ravane"]
SkillList=["Shooting","Passing","Defending"]

# For this example, we have a random number generator for our scout
# I wouldn't recommend this for an actual team
ScoresArray = np.random.randint(1,10,(4,3))

df = pd.DataFrame(data=ScoresArray, index=PlayerList, columns=SkillList)
print(df)

