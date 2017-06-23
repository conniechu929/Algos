print 'Создать приложение, реализующее хэш-таблицу для хранения строк с методом разрешения коллизий - “списки”(open hashing). В качестве хэш-функции использовать рассмотренную на лекции (слайд 12). Продемонстрировать работу разработанной ХТ. Примечание: постараться сделать ХТ самостоятельно, используя код на С++ из лекции.'


hash_table = {}


def Hash_index(string):
  total = 0
  for i in range(len(string)):
    total = total + (ord(string[i])*(i+1))
  total = total % 2069
  return total
my_str = 'abcdef'
str2 = 'lolo'

print Hash_index(my_str)



def insert(string):
  key = Hash_index(string)
  if key in hash_table:
    hash_table[key].append(string)
  else:
    hash_table[key] = [string]
  return hash_table

def search(string):
  key = Hash_index(string)
  print 'key:', key
  if key not in hash_table:
    return None
  for i in hash_table[key]:
    if i == string:
      return i

print insert(my_str)
print search(my_str)
print search(str2)
