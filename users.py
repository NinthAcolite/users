class User:
    count = 0

    def __init__(self, name, login, password, grade):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        raise Exception("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def grade(self):
        raise Exception("Неизвестное свойство grade")

    @grade.setter
    def grade(self, value):
        raise Exception("Неизвестное свойство grade")

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")

    def __lt__(self, other):
        return self._grade < other._grade

    def __le__(self, other):
        return self._grade <= other._grade

    def __eq__(self, other):
        return self._grade == other._grade

    def __ne__(self, other):
        return self._grade != other._grade

    def __gt__(self, other):
        return self._grade > other._grade

    def __ge__(self, other):
        return self._grade >= other._grade


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password, grade=None)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}, Role: {self._role}")
