
def delete_some_useles_words(stroka):
    my_list = stroka.split(' ')
    res = [i for i in my_list if 'абв' not in i ]
    return res
my_str = "141235 абвптлвыпт паврцур ырщабва 15d$$4"
print(my_str)
print(delete_some_useles_words(my_str))