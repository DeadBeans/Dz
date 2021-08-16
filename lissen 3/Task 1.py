my_list= {'один':'one',       'два':'two',        'три':'three',      'четыре':'four',     'пять':'five',
     'шесть':'six',       'семь':'seven',      'восемь':'eight',      'деваять':'nine',    'десять':'ten',
     }

def num_translate(my_list_eng):
    return my_list.get(my_list_eng)

print(num_translate('один'))

