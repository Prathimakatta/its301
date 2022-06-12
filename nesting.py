Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,4]
>>> list2=[3,5,6]
>>> list3=[7,8,9]
>>> matrix=[list1,list2,list3]
>>> matrix
[[1, 2, 4], [3, 5, 6], [7, 8, 9]]
>>> print(matrix)
[[1, 2, 4], [3, 5, 6], [7, 8, 9]]
>>> matrix[0]
[1, 2, 4]
>>> matrix[1]
[3, 5, 6]
>>> matrix[2]
[7, 8, 9]
>>> matrix[0][2]
4
>>> list=[1,2,3,4,5,6]
>>> list
[1, 2, 3, 4, 5, 6]
>>> list.append['ok']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list.append['ok']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.append9'ok'0
SyntaxError: invalid syntax
>>> list.append('ok')
>>> list
[1, 2, 3, 4, 5, 6, 'ok']
>>> list.count(5)
1
>>> list.append('6')
>>> list.count(6)
1
>>> list
[1, 2, 3, 4, 5, 6, 'ok', '6']
>>> list.count(6)
1
>>> 
>>> 
>>> 
>>> x=[1,2,3,4,5]
>>> y=[5,6,7,8]
>>> x.append(y)
>>> x
[1, 2, 3, 4, 5, [5, 6, 7, 8]]
>>> x.extend(y)
>>> x
[1, 2, 3, 4, 5, [5, 6, 7, 8], 5, 6, 7, 8]
>>> x.index(9)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x.index(9)
ValueError: 9 is not in list
>>> x.index(5)
4
>>> x{5}
SyntaxError: invalid syntax
>>> x[5]
[5, 6, 7, 8]
>>> x[3]
4
>>> ls=['here','am','today','at',10.30]
>>> ls
['here', 'am', 'today', 'at', 10.3]
>>> ls.insert(1,'I')
>>> ls
['here', 'I', 'am', 'today', 'at', 10.3]
>>> ls.pop()
10.3
>>> ls
['here', 'I', 'am', 'today', 'at']
>>> la.pop(0
       ls.pop()
       
SyntaxError: invalid syntax
>>> ls.pop()
'at'
>>> ls
['here', 'I', 'am', 'today']
>>> ls.pop(3)
'today'
>>> ls
['here', 'I', 'am']
>>> 
>>> 
>>> ls.sort()
>>> ls
['I', 'am', 'here']
>>> ls=[1,7,3,8,0,5]
>>> ls.sort()
>>> ls
[0, 1, 3, 5, 7, 8]
>>> ls.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ls.sort(reverse=true)
NameError: name 'true' is not defined
>>> ls
[0, 1, 3, 5, 7, 8]
>>> la.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    la.sort(reverse=True)
NameError: name 'la' is not defined
>>> ['here', 'I', 'am', 'today', 'at']
['here', 'I', 'am', 'today', 'at']
>>> ls.sort(reverse=True)
>>> ls
[8, 7, 5, 3, 1, 0]
>>> ls=[1,2,3,4]
>>> ls2=ls.sort()
>>> ls
[1, 2, 3, 4]
>>> ls2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ls2=ls.copy()
>>> ls2
[1, 2, 3, 4]
>>> ls=[1,2,3,4]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ls=[3,6,2,5,1]
>>> ls
[3, 6, 2, 5, 1]
>>> ls2=[item**2 for item in ls]
>>> ls2
[9, 36, 4, 25, 1]
>>> ls3=[fa/3 for fa in ls]
>>> ls3
[1.0, 2.0, 0.6666666666666666, 1.6666666666666667, 0.3333333333333333]
>>> 
>>> 
>>> 
>>> ls4=[a,b,c,d]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    ls4=[a,b,c,d]
NameError: name 'a' is not defined
>>> ls4=['a','b','c','d']
>>> ls5=[item*2 for item in ls4]
>>> ls5
['aa', 'bb', 'cc', 'dd']
>>> ls=[1,2,3,4,5]
>>> ls2=[item*10 for item in ls]
>>> ls2
[10, 20, 30, 40, 50]
>>> ls3=[item+1 for item in ls2]
>>> ls3
[11, 21, 31, 41, 51]
>>> s.center(20,'a')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    s.center(20,'a')
NameError: name 's' is not defined
>>> ls=@
SyntaxError: invalid syntax
>>> ls='hello again'
>>> ls.center(20,'a')
'aaaahello againaaaaa'
>>> ls
'hello again'
>>> 'hello\thi'.expandtabs()
'hello   hi'
>>> name=('Ramana')
>>> print(name)
Ramana
>>> name.center(100)
'                                               Ramana                                               '
>>> name.center(80)
'                                     Ramana                                     '
>>> name.center(60.'')
SyntaxError: invalid syntax
>>> name.center(60, ' ')
'                           Ramana                           '
>>> 
>>> 
>>> 
>>> 
>>> name 'Ramana Maharshi'
SyntaxError: invalid syntax
>>> name='Ramana Maharshi'
>>> name.upper()
'RAMANA MAHARSHI'
>>> name.lower()
'ramana maharshi'
>>> name[0].isupper()
True
>>> name.isupper(0
	     na
	     
SyntaxError: invalid syntax
>>> 
>>> name.isupper()
False
>>> name.islower()
False
>>> st='entitiy' '%100'
>>> st.split()
['entitiy%100']
>>> st.split('n')
['e', 'titiy%100']
>>> st.split('%')
['entitiy', '100']
>>> Sname[0].isupper()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    Sname[0].isupper()
NameError: name 'Sname' is not defined
>>> st.split('i')
['ent', 't', 'y%100']
>>> st.partition('t')
('en', 't', 'itiy%100')
>>> st.partition('100')
('entitiy%', '100', '')
>>> st.partition('10')
('entitiy%', '10', '0')
>>> st.partition('1')
('entitiy%', '1', '00')
>>> st.partition('0')
('entitiy%1', '0', '0')
>>> 
>>> 
>>> 
>>> 
>>> st.partition('%')
('entitiy', '%', '100')
>>> 
>>> 
>>> 

>>> salary='15,000'
>>> tax_rate='15%'
>>> tax='salary*tax_rate'
>>> tax=
SyntaxError: invalid syntax
>>> tax
'salary*tax_rate'
>>> print('tax')
tax
>>> salary=[15,000]
>>> tax_rate=[%15]
SyntaxError: invalid syntax
>>> tax_rate=['%15']
>>> tax=['salary*tax_rate']
>>> tax
['salary*tax_rate']
>>> salary=['15,000']
>>> tax
['salary*tax_rate']
>>> salary=(15,000)
>>> tax
['salary*tax_rate']
>>> salary=15,000
>>> tax_rate=11%
SyntaxError: invalid syntax
>>> tax_rate='10%'
>>> 