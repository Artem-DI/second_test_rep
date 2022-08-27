'''import json

login = input('Придумайте логин:\n')
passwd = input('Придумайте пароль:\n')
d = {}


def register(login, passwd):                    #ниже есть вопрос
	with open('use.json', 'a') as f:
		d[login] = passwd
		json.dump(d, f)

register(login, passwd)'''








#один из вариантов того, как я пытался реализовать проверку на совпадение логина

'''import json

login = input('Придумайте логин:\n')
passwd = input('Придумайте пароль:\n')
d = {}
with open('use.json', 'a') as f:
	json.dump(d, f)


def register(login, passwd):
	with open('use.json', 'r') as f:
		data = json.load(f)
		if login in data:
			print("Логин занят")
		else:
			with open('use.json', 'a') as f:
				d[login] = passwd
				json.dump(d, f)

register(login, passwd)
'''
'''Я долго думал как реализовать два последующих задания, но так и не смог.
Вечно создаются лишние скобки в файле, либо какая-то ошибка(ниже её приведу). 
Объясните пожалуйста.

Та самая ощибка: 

 Traceback (most recent call last):
  File "d:\python учёба\task_3_part_4.py", line 20, in <module>
    register(login, passwd)
  File "d:\python учёба\task_3_part_4.py", line 12, in register
    data = json.load(f)
  File "C:\Users\Артем\AppData\Local\Programs\Python\Python310\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
  File "C:\Users\Артем\AppData\Local\Programs\Python\Python310\lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Артем\AppData\Local\Programs\Python\Python310\lib\json\decoder.py", line 340, in decode
    raise JSONDecodeError("Extra data", s, end)
json.decoder.JSONDecodeError: Extra data: line 1 column 3 (char 2)'''