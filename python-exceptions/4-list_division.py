#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            if (int(result) % result != 0):
                raise ValueError():
            s.append(result)
        except ValueError as e:
            s.append(0)
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
    finally:
        return s
