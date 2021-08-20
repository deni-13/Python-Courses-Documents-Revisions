
#%%
#sinus grafigi ---> line plot

from numpy import sin
from matplotlib import pyplot

x=[x*0.1 for x in range(100)]
y=sin(x)


pyplot.plot(x,y)
pyplot.show()

#%%
#scatter plot
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import randn 
x=20+randn(1000)+100  


y=x+(10*randn(1000)+50)

pyplot.scatter(x,y)
pyplot.show()

#korealsyon ve dagılım grafigi


#eda'da cok kullailir.

#%%
#barplot

#mean , ort gibiler icin

#histogram --Ayrık hale getirir.

#frekans

pn=sns.load_dataset("penguins")
pn.head()
pn.describe().T
sns.histplot(data=pn,x="flipper_length_mm")













