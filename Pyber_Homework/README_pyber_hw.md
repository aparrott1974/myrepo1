

```python
# import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
    
```


```python
# get teh data
city_data = "raw_data/city_data.csv"
ride_data = "raw_data/ride_data.csv"

cdata = pd.read_csv(city_data)
rdata = pd.read_csv(ride_data)
```


```python
observed in the data:
    the higher the population density, the more rides and lower fares
    much higher variation in rural data than suburban or urban
    
```


```python
# look at the data

# len(rdata) = 2375
# len(cdata) = 126
# cdata columns: city, driver_count, type
# rdata columns:  city, date, fare, ride_id
# i'm going to left join cdata to rdata

```


```python
data = pd.merge(rdata, cdata, how='left', on='city')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
      <td>35</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
      <td>68</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# need the groups
    # Average Fare ($) Per City
    # Total Number of Rides Per City
    # Total Number of Drivers Per City
    # City Type (Urban, Suburban, Rural)
```


```python
# df[df['ids'].str.contains("ball")]
fare_u=data[data['type'].str.contains("Urban")]
fare_s=data[data['type'].str.contains("Suburban")]
fare_r=data[data['type'].str.contains("Rural")]
# fare_s.head()
```


```python
# average fair by city
avg_fare=rdata.groupby('city')['fare'].mean()
# avg_fare # uncomment to see data

avg_fare_u=fare_u.groupby('city')['fare'].mean()
avg_fare_s=fare_s.groupby('city')['fare'].mean()
avg_fare_r=fare_r.groupby('city')['fare'].mean()
# avg_fare_u

```


```python
# count of rides by city
cnt_rides=rdata.groupby('city')['ride_id'].count()
# cnt_rides # uncomment to see data

cnt_u=data[data['type'].str.contains("Urban")]
cnt_s=data[data['type'].str.contains("Suburban")]
cnt_r=data[data['type'].str.contains("Rural")]
# cnt_r
```


```python
cnt_rides_u=cnt_u.groupby('city')['ride_id'].count()
cnt_rides_s=cnt_s.groupby('city')['ride_id'].count()
cnt_rides_r=cnt_r.groupby('city')['ride_id'].count()
# cnt_rides_r
```


```python
sum_fare=rdata.groupby('city')['fare'].sum()
```


```python
cnt_drivers=cdata.groupby('city')['driver_count'].sum()
```


```python
rides_fares_df = pd.concat([cnt_rides, avg_fare], axis=1).reset_index()
# rides_fairs_df.head()  # uncomment to see data
```


```python
# rename the columns
rides_fares_df.columns=('city','Total Number of Rides Per City','Average Fare ($) Per City')
# rides_fairs_df.head() # uncomment to see data
```


```python
plt_data = pd.merge(cdata, rides_fares_df, how='left', on='city')
plt_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>Total Number of Rides Per City</th>
      <th>Average Fare ($) Per City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>28</td>
      <td>21.806429</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
      <td>26</td>
      <td>25.899615</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
      <td>22</td>
      <td>26.169091</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
      <td>29</td>
      <td>22.330345</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
      <td>23</td>
      <td>21.332609</td>
    </tr>
  </tbody>
</table>
</div>




```python


fig, ax = plt.subplots()

plt.scatter(cnt_rides_u,avg_fare_u, c='gold', s=cnt_drivers, alpha=0.5, label='Urban')
plt.scatter(cnt_rides_s,avg_fare_s, c='lightskyblue', s=cnt_drivers, alpha=0.5, label='Suburban')
plt.scatter(cnt_rides_r,avg_fare_r, c='lightcoral', s=cnt_drivers, alpha=0.5, label='Rural')
ax.set_xlabel(r'Total Number of Rides Per City', fontsize=15)
ax.set_ylabel(r'Average Fare ($) Per City', fontsize=15)
ax.set_title('Ride Count and Fare', fontsize=15)
ax.legend()
plt.show
```




    <function matplotlib.pyplot.show>




![png](output_15_1.png)



```python
# help(plt.scatter)
```


```python
# % of Total Fares by City Type
fare_type=data.groupby('type')['fare'].sum()
# fare_type
```


```python
# % of Total Rides by City Type
ride_type=data.groupby('type')['ride_id'].count()
# ride_type
```


```python
# % of Total Drivers by City Type
driver_type=data.groupby('type')['driver_count'].sum()
# driver_type
```


```python
# Labels for the sections of our pie chart
labels = ["Rural", "Suburban", "Urban"]

# The colors of each section of the pie chart
colors = ["gold", "lightskyblue", "lightcoral"]

# Tells matplotlib to seperate the "Python" section from the others
# explode = (0.1, 0, 0, 0)
```


```python
# Creates the pie chart based upon the values above

plt.pie(driver_type, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
plt.title('Count of Drivers')
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")

#title
# plt.set_title("Matplotlib bakery: A pie")

# Prints our pie chart to the screen
plt.show()
```


![png](output_21_0.png)



```python
# Creates the pie chart based upon the values above

plt.pie(ride_type, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
plt.title('Count of rides')
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")

# Prints our pie chart to the screen
plt.show()
```


![png](output_22_0.png)



```python
# Creates the pie chart based upon the values above

plt.pie(fare_type, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
plt.title('Sum of Fare')
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")

# Prints our pie chart to the screen
plt.show()
```


![png](output_23_0.png)

