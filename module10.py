import matplotlib.pyplot as plt

fig, figure = plt.subplots()

data = {
	"Hamburger": 139,
	"Hotdog": 216,
	"Cheeseburger": 182,
	"Chili Cheese Dog": 57
}

x_axis_data = data.keys()
y_axis_data = data.values()

figure.bar(x_axis_data, y_axis_data)

figure.set(ylim=[0,250],
	ylabel= 'Number of Orders',
	xlabel = 'Menu Item',
	title = 'Number of Orders for each Menu Item at the Baseball Game')



import numpy as np
import pandas as pd
from plotline import *
from ggplot import *
scores = pd.read_csv('C://Users//caitl//Documents//scores.csv')
ggplot(aes(x='Hours_Studied',y='Score_On_Exam'), data=scores)+geom_point()

plt.show()