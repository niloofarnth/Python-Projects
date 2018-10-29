import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = '/Users/niloofartehrani/Google Drive File Stream/My Drive/Programming/data-analysis/Titanic_data/titanic_data.csv'
Titanic_data = pd.read_csv(filename)

'''explanation of the column headers:
    
Variable	Definition	Key
survival	Survival	0 = No, 1 = Yes
pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
sex	Sex	
Age	Age in years	
sibsp	# of siblings / spouses aboard the Titanic	
parch	# of parents / children aboard the Titanic	
ticket	Ticket number	
fare	Passenger fare	
cabin	Cabin number	
embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton
'''

'''Questions:
    1: how did the survival changed with sex?
    2. how did survival changes with age?
    3. is there any connection between the survival and the number of parch sibsp? I should do other statistical processes on this
    4. 
    '''
 
Titanic_df = pd.DataFrame (Titanic_data)

#change some data types 


'''''''''''' 
#extracting custom DF from the main DF
survived = Titanic_df.loc[Titanic_df['Survived'] == 1]
not_survived = Titanic_df.loc[Titanic_df['Survived'] == 0]

#counting the number of m and f in the survived and not-survived 
sex_survived  = (survived['Sex'].value_counts())
sex_not_survived = not_survived['Sex'].value_counts()
sex_survival = pd.concat([sex_survived ,sex_not_survived], axis =1)
sex_survival.columns = ['Survived', 'Not Survived']


#plot the sex-based survival 

plot1 = sex_survival.plot(kind = 'bar' , rot = 0)
plot1.set_xlabel('Sex')
plot1.set_ylabel('Count')


#plot the age-based survival 

fig, plot2 = plt.subplots()
colors = ['b','g']
plot2.hist([survived['Age'].dropna(), not_survived['Age'].dropna()],color=colors, label=['Survived', 'Not Survived'], bins=16)
plot2.set_xlabel('Age')
plot2.set_ylabel('Count')
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()

#counting the number of Pclasses in the survived and not-survived 
class_survived  = (survived['Pclass'].value_counts())
class_not_survived = not_survived['Pclass'].value_counts()
class_survival = pd.concat([class_survived, class_not_survived], axis = 1)
class_survival.columns = ['Survived', 'Not Survived']

#plot the Pclas- based survival

plot3 = class_survival.plot(kind = 'bar' , rot = 0)
plot3.set_xlabel('Cabin Class')
plot3.set_ylabel('Count')



#plot histogram of the survival based on the Parch and SibSp
fig, plot4 = plt.subplots()
colors = ['b','g', 'r', 'm']
plot4.hist([survived['Parch'],not_survived['Parch'],survived['SibSp'],not_survived['SibSp']],\
            color=colors, label=['Parch Survived', 'Parch Not Survived', 'SibSp Survived' , 'SibSp Not Survived'], bins=10)
plot4.set_xlabel('Number of Parent/Children/Sibling/Spouse')
plot4.set_ylabel('Count')
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()




