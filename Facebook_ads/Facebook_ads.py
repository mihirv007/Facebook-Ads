import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

dataset=pd.read_csv('/Users/mihirverma/Facebook_ads/facebook_ads.csv')

Total_number_of_rounds=500

Number_of_ads=10

selected_ads=[]

number_of_selection=[0]*Number_of_ads

sum_of_rewards=[0]*Number_of_ads

total_rewards=0


def upper_confidence_bound_fuction():

    global total_rewards

    for n in range(0,Total_number_of_rounds):
        ad=0
        max_upper_confidence_bound=0
        for i in range(Number_of_ads):
            if (number_of_selection[i]>0):
                avg_reward=sum_of_rewards[i]/number_of_selection[i]
                delta_i=math.sqrt(((3/2)*math.log(n+1)/number_of_selection[i]))
                upper_confidence_bound=avg_reward+delta_i

            else:
                upper_confidence_bound=1e300
            if(upper_confidence_bound>max_upper_confidence_bound):
                max_upper_confidence_bound=upper_confidence_bound
                ad=i

        selected_ads.append(ad)

        number_of_selection[ad]=number_of_selection[ad]+1
        temp_rewards=dataset.values[n,ad]

        sum_of_rewards[ad]=sum_of_rewards[ad]+temp_rewards

        total_rewards=total_rewards+temp_rewards

        return total_rewards

upper_confidence_bound_fuction()
plt.hist(selected_ads)
plt.title('number of times ad is selected')
plt.xlabel('number of ads')
plt.ylabel('selection times of each ad')
plt.show()





