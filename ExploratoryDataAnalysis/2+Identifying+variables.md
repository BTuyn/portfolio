
# 2 Identifying variables


```python
import pandas as pd
df = pd.read_csv('train.csv')
```

### Showing the types and values


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1460 entries, 0 to 1459
    Data columns (total 81 columns):
    Id               1460 non-null int64
    MSSubClass       1460 non-null int64
    MSZoning         1460 non-null object
    LotFrontage      1201 non-null float64
    LotArea          1460 non-null int64
    Street           1460 non-null object
    Alley            91 non-null object
    LotShape         1460 non-null object
    LandContour      1460 non-null object
    Utilities        1460 non-null object
    LotConfig        1460 non-null object
    LandSlope        1460 non-null object
    Neighborhood     1460 non-null object
    Condition1       1460 non-null object
    Condition2       1460 non-null object
    BldgType         1460 non-null object
    HouseStyle       1460 non-null object
    OverallQual      1460 non-null int64
    OverallCond      1460 non-null int64
    YearBuilt        1460 non-null int64
    YearRemodAdd     1460 non-null int64
    RoofStyle        1460 non-null object
    RoofMatl         1460 non-null object
    Exterior1st      1460 non-null object
    Exterior2nd      1460 non-null object
    MasVnrType       1452 non-null object
    MasVnrArea       1452 non-null float64
    ExterQual        1460 non-null object
    ExterCond        1460 non-null object
    Foundation       1460 non-null object
    BsmtQual         1423 non-null object
    BsmtCond         1423 non-null object
    BsmtExposure     1422 non-null object
    BsmtFinType1     1423 non-null object
    BsmtFinSF1       1460 non-null int64
    BsmtFinType2     1422 non-null object
    BsmtFinSF2       1460 non-null int64
    BsmtUnfSF        1460 non-null int64
    TotalBsmtSF      1460 non-null int64
    Heating          1460 non-null object
    HeatingQC        1460 non-null object
    CentralAir       1460 non-null object
    Electrical       1459 non-null object
    1stFlrSF         1460 non-null int64
    2ndFlrSF         1460 non-null int64
    LowQualFinSF     1460 non-null int64
    GrLivArea        1460 non-null int64
    BsmtFullBath     1460 non-null int64
    BsmtHalfBath     1460 non-null int64
    FullBath         1460 non-null int64
    HalfBath         1460 non-null int64
    BedroomAbvGr     1460 non-null int64
    KitchenAbvGr     1460 non-null int64
    KitchenQual      1460 non-null object
    TotRmsAbvGrd     1460 non-null int64
    Functional       1460 non-null object
    Fireplaces       1460 non-null int64
    FireplaceQu      770 non-null object
    GarageType       1379 non-null object
    GarageYrBlt      1379 non-null float64
    GarageFinish     1379 non-null object
    GarageCars       1460 non-null int64
    GarageArea       1460 non-null int64
    GarageQual       1379 non-null object
    GarageCond       1379 non-null object
    PavedDrive       1460 non-null object
    WoodDeckSF       1460 non-null int64
    OpenPorchSF      1460 non-null int64
    EnclosedPorch    1460 non-null int64
    3SsnPorch        1460 non-null int64
    ScreenPorch      1460 non-null int64
    PoolArea         1460 non-null int64
    PoolQC           7 non-null object
    Fence            281 non-null object
    MiscFeature      54 non-null object
    MiscVal          1460 non-null int64
    MoSold           1460 non-null int64
    YrSold           1460 non-null int64
    SaleType         1460 non-null object
    SaleCondition    1460 non-null object
    SalePrice        1460 non-null int64
    dtypes: float64(3), int64(35), object(43)
    memory usage: 924.0+ KB


You can also check how many missing values there are in a column using **isnull()** and **sum()**


```python
df.Fence.isnull().sum()
```




    1179



## Describe the range of each feature


```python
df.LotFrontage.max()
```




    313.0




```python
df.LotFrontage.min()
```




    21.0




```python
df.LotFrontage.describe()
```




    count    1201.000000
    mean       70.049958
    std        24.284752
    min        21.000000
    25%        59.000000
    50%        69.000000
    75%        80.000000
    max       313.000000
    Name: LotFrontage, dtype: float64



### Unique values of a column
For categorical features, you can inspect which values occur in a column, using `unique`


```python
df.MSZoning.unique()
```




    array(['RL', 'RM', 'C (all)', 'FV', 'RH'], dtype=object)




```python
df.PavedDrive.unique()
```




    array(['Y', 'N', 'P'], dtype=object)



We can also show the frequency of every value for a column.


```python
df.PavedDrive.value_counts()
```




    Y    1340
    N      90
    P      30
    Name: PavedDrive, dtype: int64



### Convert values
Often, it is easier to process your data as numbers. For instance, the feature PavedDrive has a categorical label, bit of we want to use it in a regression algorithm we need to convert it to a number. In this case we convert it in the following way: N=0, P=1, Y=2 (assuming P means something like Partial).


```python
paved_drive = {'N':0, 'P':1, 'Y':2} # setup a dictionary to do the conversion

def convert_paved_drive(p):
    return paved_drive[p] # return the value of p in paved_drive dict

convert_paved_drive('P') # returns 1 because P is at position 1 in the array (indexing starts at 0)
```




    1



We can use Python's **map()** function to apply a function to every element in a collection (or more formally, an iterable). Note that we could alternatively pass the dictionary paved_drive to the map() function, since map() also accepts dictionaries.


```python
df['PavedDriveN'] = df.PavedDrive.map(convert_paved_drive)
```


```python
df.PavedDriveN[df.PavedDriveN < 2][:10]
```




    21     0
    30     0
    39     0
    41     1
    48     0
    61     0
    88     0
    97     1
    106    0
    108    0
    Name: PavedDriveN, dtype: int64



#### Assignment:  convert KitchenQual to a number. In the description of the dataset it reads that the labels mean:

|Label|description|
|:---|---|
|Ex|Excellent|
|Gd|Good|
|TA|Typical/Average|
|Fa|Fair|
|Po|Poor|


```python

```


```python
Kitchen_Qual = {'Po':0, 'Fa':1, 'TA':2, 'Gd':3,'Ex':4} # setup a dictionary to do the conversion

def convert_kitchen_qual(p):
    return Kitchen_Qual[p]


df['KitchenQual']=df.KitchenQual.map(convert_kitchen_qual)
```


```python
print(df['KitchenQual'])
```

    0       3
    1       2
    2       3
    3       3
    4       3
    5       2
    6       3
    7       2
    8       2
    9       2
    10      2
    11      4
    12      2
    13      3
    14      2
    15      2
    16      2
    17      2
    18      3
    19      2
    20      3
    21      3
    22      3
    23      2
    24      3
    25      3
    26      3
    27      3
    28      2
    29      1
           ..
    1430    2
    1431    2
    1432    2
    1433    2
    1434    2
    1435    3
    1436    2
    1437    4
    1438    2
    1439    2
    1440    2
    1441    3
    1442    4
    1443    1
    1444    3
    1445    2
    1446    2
    1447    3
    1448    2
    1449    4
    1450    2
    1451    4
    1452    2
    1453    2
    1454    3
    1455    2
    1456    2
    1457    3
    1458    3
    1459    2
    Name: KitchenQual, Length: 1460, dtype: int64



```python

```

### Add features

We can add new features to the Dataframe by simply assigning a value to it. In this example we will compute the sum of the 1st floor space and 2nd floor space.


```python
# note you need to index these with [''] because in Python variable names cannot start with a number.
df['2FlrSF'] = df['1stFlrSF'] + df['2ndFlrSF']
df['2FlrSF'][:10]
```




    0    1710
    1    1262
    2    1786
    3    1717
    4    2198
    5    1362
    6    1694
    7    2090
    8    1774
    9    1077
    Name: 2FlrSF, dtype: int64




```python
# alternatively, give a list of columns.
df[['1stFlrSF', '2ndFlrSF', '2FlrSF']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1stFlrSF</th>
      <th>2ndFlrSF</th>
      <th>2FlrSF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>856</td>
      <td>854</td>
      <td>1710</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1262</td>
      <td>0</td>
      <td>1262</td>
    </tr>
    <tr>
      <th>2</th>
      <td>920</td>
      <td>866</td>
      <td>1786</td>
    </tr>
    <tr>
      <th>3</th>
      <td>961</td>
      <td>756</td>
      <td>1717</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1145</td>
      <td>1053</td>
      <td>2198</td>
    </tr>
    <tr>
      <th>5</th>
      <td>796</td>
      <td>566</td>
      <td>1362</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1694</td>
      <td>0</td>
      <td>1694</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1107</td>
      <td>983</td>
      <td>2090</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1022</td>
      <td>752</td>
      <td>1774</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1077</td>
      <td>0</td>
      <td>1077</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1040</td>
      <td>0</td>
      <td>1040</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1182</td>
      <td>1142</td>
      <td>2324</td>
    </tr>
    <tr>
      <th>12</th>
      <td>912</td>
      <td>0</td>
      <td>912</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1494</td>
      <td>0</td>
      <td>1494</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1253</td>
      <td>0</td>
      <td>1253</td>
    </tr>
    <tr>
      <th>15</th>
      <td>854</td>
      <td>0</td>
      <td>854</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1004</td>
      <td>0</td>
      <td>1004</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1296</td>
      <td>0</td>
      <td>1296</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1114</td>
      <td>0</td>
      <td>1114</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1339</td>
      <td>0</td>
      <td>1339</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1158</td>
      <td>1218</td>
      <td>2376</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1108</td>
      <td>0</td>
      <td>1108</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1795</td>
      <td>0</td>
      <td>1795</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1060</td>
      <td>0</td>
      <td>1060</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1060</td>
      <td>0</td>
      <td>1060</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1600</td>
      <td>0</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>26</th>
      <td>900</td>
      <td>0</td>
      <td>900</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1704</td>
      <td>0</td>
      <td>1704</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1600</td>
      <td>0</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>29</th>
      <td>520</td>
      <td>0</td>
      <td>520</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>734</td>
      <td>1104</td>
      <td>1838</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>958</td>
      <td>0</td>
      <td>958</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>968</td>
      <td>0</td>
      <td>968</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>962</td>
      <td>830</td>
      <td>1792</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>1126</td>
      <td>0</td>
      <td>1126</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>1537</td>
      <td>0</td>
      <td>1537</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>864</td>
      <td>0</td>
      <td>864</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>1932</td>
      <td>0</td>
      <td>1932</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>1236</td>
      <td>0</td>
      <td>1236</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>1040</td>
      <td>685</td>
      <td>1725</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>1423</td>
      <td>748</td>
      <td>2171</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>848</td>
      <td>0</td>
      <td>848</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>1026</td>
      <td>981</td>
      <td>2007</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>952</td>
      <td>0</td>
      <td>952</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>1422</td>
      <td>0</td>
      <td>1422</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>913</td>
      <td>0</td>
      <td>913</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>1188</td>
      <td>0</td>
      <td>1188</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>1220</td>
      <td>870</td>
      <td>2090</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>796</td>
      <td>550</td>
      <td>1346</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>630</td>
      <td>0</td>
      <td>630</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>896</td>
      <td>896</td>
      <td>1792</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>1578</td>
      <td>0</td>
      <td>1578</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>1072</td>
      <td>0</td>
      <td>1072</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>1140</td>
      <td>0</td>
      <td>1140</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>1221</td>
      <td>0</td>
      <td>1221</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>953</td>
      <td>694</td>
      <td>1647</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>2073</td>
      <td>0</td>
      <td>2073</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>1188</td>
      <td>1152</td>
      <td>2340</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>1078</td>
      <td>0</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>1256</td>
      <td>0</td>
      <td>1256</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 3 columns</p>
</div>



### Code book

Write a code book. A book in which you list some collections specifics, such as the number of samples, and for every variable a description, datatype, numeric/categorical, #missing values, the value range, an example of a value. After the analysis, you can include the distribution over each variable, how the data was cleaned (missing values and outliers) and transformed. Include every operation done on the data to allow exact replication of these steps.

| variable | description | datatype | numeric/categorical | #missing | range | example value |
|--|--|--|--|--:|:-:|--|
| 1stFlrSF | First Floor square feet | int | Numeric | 0 | 334-4602 | 334 |
| 2FlrSF | Sum First Floor + Second Floor Square Feet | int | Numeric | 0 | 334-5642 | 5642 |
| PavedDriveN | State of driveway | int | numeric | 0 | 0-2 (gravel/dirt, partially paved, paved)| 2 |
| PavedDrive | State of driveway | text | Categorical | 0 | N, P, Y (gravel/dirt, partially paved, paved) | N |
| BsmtQual | Height of the basement | text | Categorical | 37 | Ex, Gd, TA, Fa, Po, NA (Excellent 100+", Good 90-99", Typical 80-89", Fair 70-79", Poor <70", No Basement | Ex |

#### Assignment: Add KitchenQual to the Code Book

| variable | description | datatype | numeric/categorical | #missing | range | example value |
|--|--|--|--|--:|:-:|--|
| 1stFlrSF | First Floor square feet | int | Numeric | 0 | 334-4602 | 334 |
| 2FlrSF | Sum First Floor + Second Floor Square Feet | int | Numeric | 0 | 334-5642 | 5642 |
| PavedDriveN | State of driveway | int | numeric | 0 | 0-2 (gravel/dirt, partially paved, paved)| 2 |
| PavedDrive | State of driveway | text | Categorical | 0 | N, P, Y (gravel/dirt, partially paved, paved) | N |
| BsmtQual | Height of the basement | text | Categorical | 37 | Ex, Gd, TA, Fa, Po, NA (Excellent 100+", Good 90-99", Typical 80-89", Fair 70-79", Poor <70", No Basement | Ex |
| KitchenQual | Quality of kitchen | int | numeric | 0 | Ex, Gd, TA, Fa, Po,(Excellent(4), Good(3), Typical(2), Fair(1), Poor(0),| 4 |
