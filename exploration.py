import numpy as np
import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

jj_counts = data["JJ"].value_counts()
sch_counts = data["SCH_STATUS_MAGNET"].value_counts()
print(jj_counts)

jj_df = pd.pivot_table(data, values=["TOT_ENE_M", "TOT_ENE_F"], index="JJ", aggfunc=np.sum)

sch_df = pd.pivot_table(data, values=["TOT_ENE_M", "TOT_ENE_F"], index="SCH_STATUS_MAGNET", aggfunc=np.sum)

print (" Total number of girls {}".format(data["TOT_ENR_F"].sum()))

print (" Total number of boys {}".format(data["TOT_ENR_M"].sum()))

print ("Ratio of girls in SCH {}".format((20499/data["TOT_ENR_F"].sum())*100))

print ("Ratio of boys in SCH {}".format((21500/data["TOT_ENR_M"].sum())*100))

print ("Ratio of girls in JJ {}".format((77/data["TOT_ENR_F"].sum())*100))

print ("Ratio of boys in JJ {}".format((427/data["TOT_ENR_M"].sum())*100))