def letters(ptr):
    ptr = ptr.lower()
    cnt_1 = 0
    cnt_2 = 0
    for itr in ptr:
        if itr == 'а' or itr == 'е' or itr == 'ё' or itr == 'и' or itr == 'о' or itr == 'у' or itr == 'э' or itr == 'ю' or itr == 'я' or itr == 'ы':
            cnt_1 += 1
        if itr == 'б' or itr == 'в' or itr == 'г' or itr == 'д' or itr == 'ж' or itr == 'з' or itr == 'й' or itr == 'к' or itr == 'л' \
                or itr == 'м' or itr == 'н' or itr == 'п' or itr == 'р' or itr == 'с' or itr == 'т' or itr == 'ф' or itr == 'х' or itr == 'ц'\
                or itr == 'ч' or itr == 'ш' or itr == 'щ' or itr == 'ъ' or itr == 'ь' or itr == 'ф' or itr == 'х':
            cnt_2 += 1
    print(cnt_1,cnt_2)

ptr = str(input())

letters(ptr)