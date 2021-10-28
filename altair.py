import pandas as pd
import numpy as np
import altair as alt
import os
import re

root_file = r".\eco\05"
file_list = os.listdir(root_file)

all_phases = []
phase1 = []
phase2 = []
phase3 = []
for file in file_list:
    path = os.path.join(root_file,file)
    data = pd.read_csv(path,header=None)
    all_phases.append(data[0].mean())
    phase1.append(data[1].mean())
    phase2.append(data[2].mean())
    phase3.append(data[3].mean())
    
x_time = pd.to_datetime(np.array([re.findall(r"(.*).csv",i) for i in file_list]).flatten())
data = pd.DataFrame()
data["date"] = x_time 
data["Sum_of_real_power_over_all_phases"] = all_phases
data["month"] = data["date"].dt.month

brush = alt.selection(type='interval')
line = alt.Chart(data,height=500,width=700).mark_line().encode(
    x='date',
    y='Sum_of_real_power_over_all_phases',
    tooltip=["Sum_of_real_power_over_all_phases","month"]
).interactive()
line

scatter = alt.Chart(data,height=500,width=700).mark_point().encode(
x="date",
y="Sum_of_real_power_over_all_phases",color="month",
    tooltip=["Sum_of_real_power_over_all_phases","month"]).interactive()
(line + scatter).save("code.html")
line + scatter