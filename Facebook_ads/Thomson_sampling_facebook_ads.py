import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random 

dataset=pd.read_csv('/Users/mihirverma/Facebook_ads/facebook_ads.csv')

total_Numbers_Of_Rounds=1000

number_Ads=10

selected_Ads=[]

number_Of_Reward_1=[0]*10

number_Of_Reward_0=[0]*10

total_Number_Of_Rewards=0



for num in range(0,total_Numbers_Of_Rounds):
    ad=0
    max_Random=0

    for i in range(0,number_Ads):
        beta_Variant=random.betavariate(number_Of_Reward_0[i]+1 ,number_Of_Reward_1[i]+1)

        if (beta_Variant>max_Random):
            max_Random=beta_Variant
            ad=i
        
    selected_Ads.append(ad)
    reward=dataset.values[num,ad]

    if reward==1:
        number_Of_Reward_1[ad]=number_Of_Reward_1[ad]+1
    
    else:
        number_Of_Reward_0[ad]=number_Of_Reward_0[ad]+1
    
    total_Number_Of_Rewards=total_Number_Of_Rewards+reward


plt.hist(selected_Ads)
plt.title('thomson sampling algorithm')
plt.xlabel('number of ads')
plt.ylabel('number of selected ads')
plt.show()


