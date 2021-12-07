"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    # Creating counter var
    counter = [0]
    # Coping decorated class init
    cls_init = cls.__init__

    def get_created_instances(cls):
        return counter[0]

    def reset_instances_counter(cls):
        temp = counter[0]
        counter[0] = 0
        return temp

    # Increase counter var in class init
    def __init__(self, *args, **kwargs):
        cls_init(self, *args, **kwargs)
        counter[0] = counter[0] + 1

    # Initializing funcs as decorated class methods,
    # new init with counter as decorated class init
    cls.get_created_instances = classmethod(get_created_instances)
    cls.reset_instances_counter = classmethod(reset_instances_counter)
    cls.__init__ = __init__

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
