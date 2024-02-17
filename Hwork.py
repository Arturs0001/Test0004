class BaseClass1:
    def __init__(self):
        self.exclusive_attr1 = "Exclusive Attribute 1 from BaseClass1"

    def exclusive_method1(self):
        return


class BaseClass2:
    def __init__(self):
        self.exclusive_attr2 = "Exclusive Attribute 2 from BaseClass2"

    def exclusive_method2(self):
        return


class ResultClass(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        self.result_attr = "Result Class Attribute"

    def result_method(self):
        return


result_obj = ResultClass()
print(result_obj.exclusive_attr1)
print(result_obj.exclusive_method1())
print(result_obj.exclusive_attr2)
print(result_obj.exclusive_method2())
print(result_obj.result_attr)
print(result_obj.result_method())

import random


class NumberEncryptor:
    def __init__(self, number):
        self._number = number
        self._encrypt()

    def _encrypt(self):
        self._number *= random.randint(1, 10)

    def __str__(self):
        return str(self._number)


original_number = 42
encrypted_obj = NumberEncryptor(original_number)
print(f"Original number: {original_number}")
print(f"Encrypted object: {encrypted_obj}")


result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
