
print("Урок 3. Пункт 2")


def user_data(name, family_name, data_birth, city, email, phone):
    user_data_result = ' '.join([name, family_name, data_birth, city, email, phone])
    return user_data_result


print(user_data(name=input("Введите, пожалуйста, имя:"), family_name=input("Введите, пожалуйста, фамилию:"),
                data_birth=input("Введите, пожалуйста, год рождения:"),
                city=input("Введите, пожалуйста, город проживания:"),
                email=input("Введите, пожалуйста, email:"), phone=input("Введите, пожалуйста, телефон:")))
