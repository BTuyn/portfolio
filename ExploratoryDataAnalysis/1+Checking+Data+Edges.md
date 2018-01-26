
# 1. Checking data edges


```python
import pandas as pd
df = pd.read_csv('train.csv')
```

Pandas reads the file as a `Dataframe` object, which resembles a table in a database. The header (first line) provides the column labels, and every row in the file is inserted as a row in the Dataframe. We can view the first view lines with the `head()` method. You can also use `head(n)` to show the first `n` lines.

### the number of rows of a dataframe

If you know how many samples there should be (for instance from the source where you obtained the data) check it.

#### Assignment: Enter code to get the number of rows in the dataframe using the len() function, the correct answer should be 1460.


```python
len(df)
```




    1460



### columns in the dataframe

Similarly, if you known how many features there should be, check it. Also check for key features that you need for the problem you want to study. In this dataset, since the task is to predict the target variable SalePrice, we would require features that we expect to be most useful such as the size of the house.


```python
df.columns
```




    Index(['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
           'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
           'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
           'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
           'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
           'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
           'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
           'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
           'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
           'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
           'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
           'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
           'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
           'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
           'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
           'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
           'SaleCondition', 'SalePrice'],
          dtype='object')



### the number of columns in a dataframe


```python
len(df.columns)
```




    81



### Inspecting the first and last rows

One of the reasons you want to inpect the first and last rows is to make sure all the data was read ok. Sometimes, files are split, meaning you end up with half a record, or someone inserted some commentary on the first or last lines.


```python
df.head() # first rows
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 81 columns</p>
</div>



#### Assignment: Enter the code to only inspect the first row, hint you can pass the number of rows to head()


```python
df.head(0)
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
<p>0 rows × 81 columns</p>
</div>



We can view the datatypes and the number of non-null values, using the `info()` method. Null refers to 'no value' or 'unkown value'.


```python
df.tail() # last 5 rows
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1455</th>
      <td>1456</td>
      <td>60</td>
      <td>RL</td>
      <td>62.0</td>
      <td>7917</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>1457</td>
      <td>20</td>
      <td>RL</td>
      <td>85.0</td>
      <td>13175</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>1458</td>
      <td>70</td>
      <td>RL</td>
      <td>66.0</td>
      <td>9042</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>1459</td>
      <td>20</td>
      <td>RL</td>
      <td>68.0</td>
      <td>9717</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>1460</td>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9937</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 81 columns</p>
</div>



### subsetting rows


```python
# select the first two rows (the upper bound is always exclusive)
df[:2]
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181500</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 81 columns</p>
</div>




```python
# select the last 2 rows, negative numbers are an index that count back from the end of the dataframe
df[-2:]
```

#### Assignment: select rows 2 and 3 in one statement


```python
df[2:4]
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 81 columns</p>
</div>



### Some additional inspections
### Subset rows by boolean indexing (logical statements)


```python
# creates a boolean index that indicates which rows have '04' in ExpMM.
df.MSZoning == 'RL'
```




    0        True
    1        True
    2        True
    3        True
    4        True
    5        True
    6        True
    7        True
    8       False
    9        True
    10       True
    11       True
    12       True
    13       True
    14       True
    15      False
    16       True
    17       True
    18       True
    19       True
    20       True
    21      False
    22       True
    23      False
    24       True
    25       True
    26       True
    27       True
    28       True
    29      False
            ...  
    1430     True
    1431     True
    1432     True
    1433     True
    1434     True
    1435     True
    1436     True
    1437     True
    1438    False
    1439     True
    1440     True
    1441    False
    1442    False
    1443     True
    1444     True
    1445     True
    1446     True
    1447     True
    1448     True
    1449    False
    1450     True
    1451     True
    1452    False
    1453     True
    1454    False
    1455     True
    1456     True
    1457     True
    1458     True
    1459     True
    Name: MSZoning, Length: 1460, dtype: bool




```python
# create a subset dataframe of only rows that contain 'IR1' for the column LotShape
dfrl = df[df.LotShape == 'IR1']
dfrl.head(4)
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>50</td>
      <td>RL</td>
      <td>85.0</td>
      <td>14115</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143000</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 81 columns</p>
</div>




```python
# create a subset dataframe of only rows that contain
# 'IR1' for the column LotShape AND '2008' for YrSold
dfrlreg = df[(df.LotShape == 'IR1') | (df.YrSold == 2008)]
dfrlreg.head(4)
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 81 columns</p>
</div>




```python
# create a subset dataframe of only rows that contain
# IR1' for the column LotShape OR '2008' for YrSold
dfrlreg = df[(df.LotShape == 'IR1') | (df.YrSold == 2008)]
dfrlreg.head(4)
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 81 columns</p>
</div>



#### Assignment: Show the sizes of the poolareas of the 7 houses that have a pool area (tip: PoolArea > 0)


```python
df[df.PoolArea >0]
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
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>197</th>
      <td>198</td>
      <td>75</td>
      <td>RL</td>
      <td>174.0</td>
      <td>25419</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>512</td>
      <td>Ex</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>235000</td>
    </tr>
    <tr>
      <th>810</th>
      <td>811</td>
      <td>20</td>
      <td>RL</td>
      <td>78.0</td>
      <td>10140</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>648</td>
      <td>Fa</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181000</td>
    </tr>
    <tr>
      <th>1170</th>
      <td>1171</td>
      <td>80</td>
      <td>RL</td>
      <td>76.0</td>
      <td>9880</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>576</td>
      <td>Gd</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>171000</td>
    </tr>
    <tr>
      <th>1182</th>
      <td>1183</td>
      <td>60</td>
      <td>RL</td>
      <td>160.0</td>
      <td>15623</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>555</td>
      <td>Ex</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>745000</td>
    </tr>
    <tr>
      <th>1298</th>
      <td>1299</td>
      <td>60</td>
      <td>RL</td>
      <td>313.0</td>
      <td>63887</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR3</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>...</td>
      <td>480</td>
      <td>Gd</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>New</td>
      <td>Partial</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1386</th>
      <td>1387</td>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>16692</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>519</td>
      <td>Fa</td>
      <td>MnPrv</td>
      <td>TenC</td>
      <td>2000</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>1423</th>
      <td>1424</td>
      <td>80</td>
      <td>RL</td>
      <td>NaN</td>
      <td>19690</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>738</td>
      <td>Gd</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>WD</td>
      <td>Alloca</td>
      <td>274970</td>
    </tr>
  </tbody>
</table>
<p>7 rows × 81 columns</p>
</div>



### Subsetting columns
More advanced subsetting can be done with df.ix. The first range selects the rows (: selects all). The second range selects columns, either by index number of label name. Somewhat confusing, the upperbounds are inclusive here.


```python
# More advanced subsetting can be done with df.ix. The first range selects the rows. 
df.ix[:5, 'LotArea':'LotShape']
```

    /opt/jupyterhub/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:2: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate_ix
      





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
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>14115</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# alternatively, give a list of columns.
df[['1stFlrSF', '2ndFlrSF']]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>856</td>
      <td>854</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1262</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>920</td>
      <td>866</td>
    </tr>
    <tr>
      <th>3</th>
      <td>961</td>
      <td>756</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1145</td>
      <td>1053</td>
    </tr>
    <tr>
      <th>5</th>
      <td>796</td>
      <td>566</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1694</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1107</td>
      <td>983</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1022</td>
      <td>752</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1077</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1040</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1182</td>
      <td>1142</td>
    </tr>
    <tr>
      <th>12</th>
      <td>912</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1494</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1253</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>854</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1004</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1296</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1114</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1339</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1158</td>
      <td>1218</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1108</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1795</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1060</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1060</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1600</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>900</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1704</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1600</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>520</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>734</td>
      <td>1104</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>958</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>968</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>962</td>
      <td>830</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>1126</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>1537</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>864</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>1932</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>1236</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>1040</td>
      <td>685</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>1423</td>
      <td>748</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>848</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>1026</td>
      <td>981</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>952</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>1422</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>913</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>1188</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>1220</td>
      <td>870</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>796</td>
      <td>550</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>630</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>896</td>
      <td>896</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>1578</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>1072</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>1140</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>1221</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>953</td>
      <td>694</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>2073</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>1188</td>
      <td>1152</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>1078</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>1256</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 2 columns</p>
</div>


