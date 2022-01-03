class UserIo:
    @staticmethod
    def get_username():
        while True:
            user_name = input('Введите имя профиля: ')
            if user_name == '':
                print('Введено некорректное имя профиля.')
            else:
                return user_name

    @staticmethod
    def get_photo_count():
        while True:
            try:
                photo_count = int(input('Введите число фотографий: '))
                if photo_count >= 0:
                    return photo_count
            except ValueError:
                pass
            print('Введено некорректное число фотографий.')
