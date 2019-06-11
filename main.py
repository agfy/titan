import pandas
import numpy as np

data = pandas.read_csv('titan.csv', index_col='PassId')
sex = data['Sx'].value_counts()
servived = data['Survive'].value_counts(normalize=True)
pclass = data['Pclss'].value_counts(normalize=True)
mean = data['Ag'].mean()
median = data['Ag'].median()
cor = data['SbSp'].corr(data['Prch'])
name = data['Nam']
arr = np.chararray(len(data['Sx']))
arr[:] = ''
first_name = pandas.Series(arr)

for index, row in data.iterrows():
	if row['Sx'] == 'fmale':
		first_name[index] = row['Nam'][row['Nam'].index('.'):]

fname = first_name.value_counts()
