import pandas as pd 

#Series
data=pd.Series([10,20,30,40,50])
print(data)
d=pd.Series([10,20,30,40,50],index=[1,2,3,4,5])
print(d)

#Data Frames
df=pd.DataFrame(
    {
        "Product":['Mobile','Laptop','Electronics','Health','Accessories','Cloths'],
        "Price":[10000,100000,100,200,300,400],
        "Quantity":[1,2,3,4,5,6] 
    }
)
print(df)
print(df.shape)
print(df.columns)
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))
print(df.info())
print(df.describe())

#fillna() and dropna()
df1=pd.DataFrame(
    {
        "Product":['Mobile','Laptop',None,'Health','Accessories','Cloths'],
        "Price":[10000,100000,None,200,300,400],
        "Quantity":[1,2,None,4,5,6] 
    }
)
print(df1)
print(df1.fillna("OM"))
print(df1.dropna())



