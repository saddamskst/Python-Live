import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

path="C:/Users/MD SADDAM/OneDrive - 01s3y/My Courses (Content - Study Material etc.)/My Live Sessions/Python 12 Week DAMC 1.0 Special Batch/.Python-Special-Class/DA-Project/Data/Vehicles.csv"


df=pd.read_csv(path, encoding="latin-1")

plt.figure(figsize=(12,6))
# sns.histplot(df["yearOfRegistration"], kde=True, color="#ff1100")

sns.relplot(data=df, kind="line",x="yearOfRegistration", y="vehicleType", col="offerType",)

# plt.title("Distribution Data")
# plt.xlabel("Distribution")
# plt.ylabel("Qty Sales")


plt.savefig("C:/Users/MD SADDAM/OneDrive - 01s3y/My Courses (Content - Study Material etc.)/My Live Sessions/Python 12 Week DAMC 1.0 Special Batch/.Python-Special-Class/DA-Project/Data/NewChart.png")

plt.show()