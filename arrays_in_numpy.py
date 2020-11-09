import numpy as np

# Create our 2d array
WCYears = [2002,2006,2010,2014]
WCHosts = ["Japan/Korea","Germany","South Africa","Brazil"]
WCWinners = ["Brazil","Italy","Spain","Germany"]

WCArray = np.array((WCYears,WCHosts,WCWinners))

print(WCArray[2, -1])


