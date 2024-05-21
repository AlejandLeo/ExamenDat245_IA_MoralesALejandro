import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import OneHotEncoder

prepro = SimpleImputer(missing_values=np.nan,strategy="most_frequent")

datp = pd.read_csv("mxmh_survey_results1.csv",sep=";")

column=datp.columns.values
datp=prepro.fit_transform(datp)
datp=pd.DataFrame(data=datp,columns=column)

#categorizar las clases nominales con OnehotEncnoder
categoric = ['Primary streaming service','While working','Instrumentalist',
                       'Composer','Fav genre','Exploratory','Foreign languages']  
target = column[len(column)-1]

ppOHE = OneHotEncoder()
clases = ppOHE.fit_transform(datp[categoric]).toarray()
clases_names = ppOHE.get_feature_names_out(categoric)

datAdi = pd.DataFrame(clases, columns=clases_names)
data = datp.drop(columns=categoric)
data = pd.concat([data, datAdi], axis=1)


x = data.drop(columns=target)
y = data[target]

#x = datp.drop([column[len(column)-1]],axis=1).values
#y = datp[column[len(column)-1]].values

#crear y entrenar el arbol de decision
clf = DecisionTreeClassifier()
clf.fit(x, y)

plt.figure(figsize=(200,100))
plot_tree(clf, filled=True)
plt.show()

