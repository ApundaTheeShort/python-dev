my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)
extension = (50,60,70)
my_list.extend(extension)
my_list.remove(70)
my_list.sort(reverse=False)

indexOf30 = my_list.index(30)
print('Index of 30:' ,indexOf30)
