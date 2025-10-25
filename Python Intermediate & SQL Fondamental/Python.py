#create a dictionnary 
my_dict={'eleve1':'Bouba',# string 
         'eleve2':'Moise',
         'eleve3':1,#int
         'list_matiere':['maths','francais','sport','loisirs'],#list
         }
#display the differents values 
print(my_dict.get('list_matiere'))


#loop to display key and value of the differents items of the dictionnary 
for key,value in my_dict.items():
    print(f'key:{key} value:{value}')
