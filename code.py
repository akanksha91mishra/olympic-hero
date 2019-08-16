# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data=data.rename({"Total":"Total_Medals"}, axis=1)
data.head(10)


# --------------
#Code starts here




data["Better_Event"] = np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter")
data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"],"Both",data["Better_Event"])
better_event=data["Better_Event"].value_counts().index.tolist()[0]
print(better_event)


# --------------
#Code starts here




top_countries = data.filter(['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'],axis=1)

top_countries = top_countries.drop(top_countries.index[-1],axis=0)
def top_ten(top_countries,column):
    country_list = list((top_countries.nlargest(10,column)["Country_Name"]))
    return country_list

top_10_summer=top_ten(top_countries,"Total_Summer")
print(top_10_summer)
top_10_winter=top_ten(top_countries,"Total_Winter")
print(top_10_winter)
top_10=top_ten(top_countries,"Total_Medals")
print(top_10)
common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(top_10))
print(common)









# --------------
#Code starts here
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]
summer_df.groupby(["Country_Name","Total_Summer"]).size().plot(kind="bar")
winter_df.groupby(["Country_Name","Total_Winter"]).size().plot(kind="bar")
top_df.groupby(["Country_Name","Total_Medals"]).size().plot(kind="bar")


# --------------
#Code starts here
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
summer_max = summer_df.sort_values("Golden_Ratio", ascending = False)
summer_max_ratio = summer_max["Golden_Ratio"].iloc[0]
print(summer_max_ratio)
summer_country_gold = summer_max["Country_Name"].iloc[0]
print(summer_country_gold)

winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max = winter_df.sort_values("Golden_Ratio",ascending = False)
winter_max_ratio = winter_max["Golden_Ratio"].iloc[0]
print(winter_max_ratio)
winter_country_gold = winter_max["Country_Name"].iloc[0]
print(winter_country_gold)

top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
top_max = top_df.sort_values("Golden_Ratio",ascending = False)
top_max_ratio = top_max["Golden_Ratio"].iloc[0]
print(top_max_ratio)
top_country_gold = top_max["Country_Name"].iloc[0]
print(top_country_gold)


# --------------
#Code starts here




data_1 = data.drop(data.index[-1],axis=0)
data_1["Total_Points"]=data_1["Gold_Total"]*3+data_1["Silver_Total"]*2+data_1["Bronze_Total"]
most = data_1.sort_values("Total_Points", ascending=False)
most_points = most["Total_Points"].iloc[0]
best_country = most["Country_Name"].iloc[0]
print(most_points)
print(best_country)


# --------------
#Code starts here
best = data[data["Country_Name"]==best_country]
best = best.filter(['Gold_Total','Silver_Total','Bronze_Total'])
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


