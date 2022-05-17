import pandas as pd

### (1) Creating a DataFrame

Data = pd.DataFrame({'ID':[1,2,3],
                     'ANIMAL_TYPE':['Dog', 'Dog', 'Cat'],
                     'NAME':['Badook', 'Happy', 'Nero']})

Data = pd.DataFrame({'ID':[1,2,3],
                     'ANIMAL_TYPE':['Dog', 'Dog', 'Cat'],
                     'NAME':['Badook', 'Happy', 'Nero']},
                      index = [1,2,3])


### (2) view data frame
# show all data
Data

# show the index
Data.index

# show the columns
Data.columns

# show the values
Data.values


### (3) Selecting a subset of the data
# selecting the 'ID' column
Data.ID
Data['ID']

# selecting a row based on index
Data.iloc[1]

# selecting a row based on a condition
Data[Data.ANIMAL_TYPE == 'Dog']

# replace
Data.replace('Dog', 'Bear')

# dropping duplicates()
Data3 = pd.DataFrame({'ID':[1,1,2,3],
                     'ANIMAL_TYPE':['Dog','Dog','Dog','Cat'],
                     'NAME':['Badook','Badook', 'Happy', 'Nero']})
Data_new = Data3.drop_duplicates() ### nothing will happen since we do not have duplicates


### (4) count and sort
Data.groupby(by='ANIMAL_TYPE').count()  

Data.sort_values('NAME') # default values is Ture for the ascending argument
Data.sort_values('NAME', ascending=False) # so if you set as False it will be a descending sort

### (5) Merge
Data1 = pd.DataFrame({'ID':[1,2,3],
                     'ANIMAL_TYPE':['Dog', 'Dog', 'Cat'],
                     'NAME':['Badook', 'Happy', 'Nero']})

Data2 = pd.DataFrame({'ID':[1,2,4],
                     'WEIGHT':[10, 15, 2],
                     'HEIGHT':[20, 30, 20]})


merged_Data = pd.merge(Data1, Data2, how='outer')


### (6) Save data to csv
merged_Data.to_csv('test.csv')







####################################
##### In class questions
####################################
# using the two files ANIMAL_INFO.csv  &  ANIMAL_INS.csv
# code to upload the two files to CoLab
# (0) Load libraries
from google.colab import files #this is a colab specific library
import io
import pandas as pd

# (1) Prepare file
### (1.1) Upload data from local computer to colab
uploaded1 = files.upload()
uploaded2 = files.upload()

### (1.2) Read csv file
df_AnimalInfo = pd.read_csv(io.BytesIO(uploaded1['ANIMAL_INFO.csv']))
df_AnimalIns = pd.read_csv(io.BytesIO(uploaded2['ANIMAL_INS.csv']))




