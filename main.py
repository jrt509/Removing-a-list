

def list_removed(new_string):
   del new_string[0]
   del new_string[-1]

   return(new_string)

my_list = ['Thank','Goodness','It','Is','Friday']

print(list_removed(my_list))