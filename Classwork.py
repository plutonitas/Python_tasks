import re

def opening():
    file = open('Zh.html', 'r', encoding = 'utf-8')
    Zh = file.read()
    res = re.findall(r'<a href=.+>([а-я]+)</a>', Zh)
    file.close()
    fileres = open('result1', 'w', encoding = 'utf-8')
    fileres.write('\n'.join(res))
    fileres.close()
opening()

    
