import numpy as np 
# import matplotlib.pyplot as plt
import pandas as pd 
# import seaborn as sb
#%matplotlib inline
# sb.set()
test =pd.read_csv('/home/mehroz/Desktop/ml/code1/input/test.csv', encoding='utf8', engine='python')
train = pd.read_csv('/home/mehroz/Desktop/ml/code1/input/train.csv', encoding='utf8', engine='python')


# sb.countplot(x='Survived',y= train,)