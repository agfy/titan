import pandas
import numpy as np

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
sex = data['Sex'].value_counts()
servived = data['Survived'].value_counts(normalize=True)
pclass = data['Pclass'].value_counts(normalize=True)
mean = data['Age'].mean()
median = data['Age'].median()
cor = data['SibSp'].corr(data['Parch'])
name = data['Name']
arr = np.chararray(len(data['Sex']))
arr[:] = ''
first_name = pandas.Series(arr)

for index, row in data.iterrows():
	if row['Sex'] == 'female':
		first_name[index] = row['Name'][row['Name'].index('.'):]

fname = first_name.value_counts()
