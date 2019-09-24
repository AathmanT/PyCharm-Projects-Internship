import pandas as pd
df2= pd.read_csv("Dummy_data.csv")
print(df2)
df3 = pd.read_csv("Dummy_data_transformed.csv")

# print(df2.dtypes)
# print(df2['Zip Code'])
# print(df2.iloc[0])

# print(df3)

zipcode=3
days=5
for i in range(0,zipcode,1):
    for j in range(0,days,1):
        row_num=(i*days)+j
#         x=y
#         print(x,"zipcode",i)
        df3.at[row_num,'Zip Code']=df2.loc[i,"Zip Code"]
        df3.at[row_num,"Days"]=j+1
        df3.at[row_num,"Counts"]=df2.iloc[i,j+1]
print(df3)
df3.to_csv("new.csv")