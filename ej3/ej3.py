import numpy as np
import pandas as pd
import sklearn.preprocessing as prepros

dat=pd.read_csv("mxmh_survey_results1.csv",sep=";")
column=dat.columns.values
categoric = ['Primary streaming service','While working','Instrumentalist',
                       'Composer','Fav genre','Exploratory','Foreign languages'] 
print(dat.head)

pp1 =prepros.OneHotEncoder()
#x = pp1.fit_transform(dat[categoric]).toarray()
clases = pp1.fit_transform(dat[categoric]).toarray()
clases_names = pp1.get_feature_names_out(categoric)

datAdi = pd.DataFrame(clases, columns=clases_names)
dat1 = dat.drop(columns=categoric)
dat1 = pd.concat([dat, datAdi], axis=1)

#print(x)
print(dat1.head)
print(dat1.columns.values)

pp2 = prepros.KBinsDiscretizer(n_bins=5,encode="ordinal",strategy="quantile")
clases = pp2.fit_transform(dat1[categoric]).toarray()
clases_names = pp2.get_feature_names_out(categoric)

#datAdi = pd.DataFrame(clases, columns=clases_names)
#print(datAdi)