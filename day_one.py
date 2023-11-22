name='li mengda'
print(name.title())

print(name.upper())
print(name.lower())
#转化大小写

first_name='li'
last_name='mengda'
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name}")
print(f"Hello,{full_name.upper()}")
#f：在插入变量的值/直接print变量full_name

favorite_language=' python  '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
#.表示方法    ：删除数据空白


url='http://www.python.org'
print(url.removeprefix('http://www.'))

a=0.1+0.3
print(a)

Teammate=['liz','jj','xiang','lk']
print(Teammate)
print(Teammate[0],'\n',Teammate[1].strip())#value的空白无法除去
print(Teammate[1])
print(f"The members of our team are {Teammate[0].title()} {Teammate[1].title()} {Teammate[2].title()} and {Teammate[3].title()}")
T=print(f"The members of our team are {Teammate[0].title()} {Teammate[1].title()} {Teammate[2].title()} and {Teammate[3].title()}")

Guider=[]
Guider.append('Han Yiliang')
Guider.append('Li Yv')
G=print(f"Our guider are {Guider[0].title()} and {Guider[1].title()}")

print(f"{T} {G}")

Guider_new=Guider.pop()
#pop弹出元素并继续使用
print(Guider)
print(Guider_new)
