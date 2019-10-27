import numpy as np 
# import matplotlib.pyplot as plt
import pandas as pd 
# import seaborn as sb
#%matplotlib inline
# sb.set()
test =pd.read_csv('C:\Users\sheik\Desktop\ML\kaggle\Machine-learning--kaggle-titanic-progect-assignment-\input\test.csv', encoding='utf8', engine='python')
train = pd.read_csv('C:\Users\sheik\Desktop\ML\kaggle\Machine-learning--kaggle-titanic-progect-assignment-\input\train.csv', encoding='utf8', engine='python')
print test

# sb.countplot(x='Survived',y= train,)