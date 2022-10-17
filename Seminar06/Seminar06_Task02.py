# Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a_lst = ('1', "a", 'b', '2', '3', 'c')

print(tuple(filter(lambda x: x.isdigit(), a_lst)))
print(tuple(filter(lambda x: x.isalpha(), a_lst)))
