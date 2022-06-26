#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. VIsualisasi hubungan antara pegawai attrition dengan faktor antara lain
import pandas as pd

df = pd.read_csv (r'datapekerja.csv')
print (df)


# In[2]:


employee = pd.read_csv(r'datapekerja.csv', usecols=['Attrition','Department'])
employee.head()


# In[47]:


#Attrition dengan Departement
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["Department"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["Department"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Departement (Attrition Yes & No)", pad=15)
ax.set_xlabel("Departement", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[48]:


#Attrition dengan Distance From Home
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["DistanceFromHome"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["DistanceFromHome"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Distance From Home (Attrition Yes & No)", pad=15)
ax.set_xlabel("Distance From Home", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[49]:


#Attrition dengan Monthly Income
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["MonthlyIncome"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["MonthlyIncome"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Monthly Income (Attrition Yes & No)", pad=15)
ax.set_xlabel("Monthly Income", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[50]:


#Attrition dengan Job Role
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["JobRole"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["JobRole"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Job Role (Attrition Yes & No)", pad=15)
ax.set_xlabel("Job Rolee", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[51]:


#Attrition dengan Gender
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["Gender"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["Gender"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Gender (Attrition Yes & No)", pad=15)
ax.set_xlabel("Gender", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[53]:


#Attrition dengan Over Time
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["OverTime"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["OverTime"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Over Time (Attrition Yes & No)", pad=15)
ax.set_xlabel("Over Time", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[54]:


#Attrition dengan Marital Status
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["MaritalStatus"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["MaritalStatus"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Marital Status (Attrition Yes & No)", pad=15)
ax.set_xlabel("Marital Status", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[56]:


#Faktor yang paling mempengaruhi attrition
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv (r'datapekerja.csv')
yes = data[data["Attrition"] == "Yes"]
x_ye = yes["PerformanceRating"].values
y_ye = yes["Age"].values
no = data[data["Attrition"] == "No"]
x_n = no["PerformanceRating"].values
y_n = no["Age"].values

fig, ax = plt.subplots()
ax.scatter(x_n, y_n, c="r", label="No")
ax.scatter(x_ye, y_ye, c="b", label="Yes")

ax.set_title("Age vs Performance Rating (Attrition Yes & No)", pad=15)
ax.set_xlabel("Performance Rating", labelpad=15)
ax.set_ylabel("Age", labelpad=15)
ax.legend()
plt.show()


# In[86]:


#2. 
crime = pd.read_csv(r'crime.csv')
crime.head()


# In[94]:


import seaborn as sns

sns.heatmap(pd.crosstab(crime.MONTH, crime.YEAR))


# In[ ]:




