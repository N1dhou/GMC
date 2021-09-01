import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

#Reading the CSV file from a relative path
raw_data=pd.read_csv("titanic-passengers.csv", sep=';')
df=raw_data
#Getting an overview of the raw data
"""print(df.head(5))
print(df.info())
print(df.describe())"""
#Fixing the key of the dataframe
df.set_index("PassengerId",inplace=True)
df.sort_index(axis=0,inplace=True)
"""print(df.head())"""
#DATA PREPROCESSING
#cleaning data (removing NaN Values)
"""print(df.isnull().sum())"""
df.dropna(axis=1,thresh=500,inplace=True)
"""print(df["Embarked"].value_counts())"""
df["Embarked"].fillna('S',inplace=True)
"""df['Age'].fillna(df['Age'].mean() , inplace=True)
   df['Age'].fillna(df['Age'].median() , inplace=True)
   df['Age'].fillna(df['Age'].mode() , inplace=True)"""
df.dropna(axis=0,how='any',inplace=True)
"""print(df.head(5))
print(df.isnull().sum())"""
#Feature Transformation (from categorical to numerical)
encoder = LabelEncoder()
df['Embarked']=encoder.fit_transform(df['Embarked'])
print(df.head(5))
#Feature Selection (Removing unnecessary columns)
"""df=df.drop(['Name'],axis=1)
print(df.head(5))"""




#DATA VISUALIZATION
scaler = StandardScaler()
df1=df.drop(['Survived','Pclass','Sex','SibSp','Parch','Ticket','Embarked'],axis = 1)
df1["Age"] = scaler.fit_transform(df1[["Age"]].values)
df1["Fare"] = scaler.fit_transform(df1[["Fare"]].values)
sns.boxplot(data=df1)
plt.show()




grid= sns.FacetGrid(df,row="Sex",col="Survived",)
grid.map(plt.hist,"Age",bins=10)
grid.add_legend()
plt.show()




#Variables correlation map
def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
plot_correlation_map(df)
plt.show()




#4444444444444444444444444444444
cleanup={"Survived":{'yes':1,'no':0}}
df.replace(cleanup,inplace=True)
df.head()
print(df[["Pclass","Survived"]].groupby(["Pclass"],as_index=True).mean())
#555555555555555555555555555555555



Title_Dictionary = {

"Capt":       "Officer",
"Col":        "Officer",
"Major":      "Officer",
"Dr":         "Officer",
"Rev":        "Officer",

"Jonkheer":     "Royalty",
"Don":          "Royalty",
"Sir" :         "Royalty",
"Lady" :        "Royalty",
"the Countess": "Royalty",
"Dona":         "Royalty",

"Mme":        "Miss",
"Mlle":       "Miss",
"Miss" :      "Miss",

"Ms":         "Mrs",
"Mr" :        "Mrs",
"Mrs" :       "Mrs",

"Master" :    "Master"}


#666666666666666666666666666666666666666666666666