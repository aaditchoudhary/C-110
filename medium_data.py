from datetime import date
import pandas as pd
import plotly.express as px
import math
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\medium_data.csv")
rdt=df["reading_time"].tolist()

population_mean=statistics.mean(rdt)
print(population_mean)
std_dev=statistics.stdev(rdt)
print("standard deviation is",std_dev)

fig=ff.create_distplot([rdt],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="Mean"))

fig.show()

dataset=[]
for i in range(0,30):
    r=random.randint(0,len(rdt))
    value=rdt[r]
    dataset.append(value)
a = statistics.mean(dataset)
print("mean is",a)
a_stdev=statistics.stdev(dataset)
print("standard deviation is",a_stdev)
