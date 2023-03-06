#tvorba kodu, který pošle uvítací dopisy konkrétnímu uživateli


with open("Input/jmena.txt") as names_file:
    names_list = names_file.readlines()
    for i in names_list:
        i = i.strip()
        with open(f"output/guest_{i}.txt","w") as welcome_letter:
            with open("Input/zvaci_dopis.txt") as defautl_letter:
                list_of_letter = defautl_letter.read()
                welcome_letter.write(list_of_letter.replace("[name]",f"{i}"))







