#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            if (int(result) - result != 0.0):
                raise ValueError("0")
            s.append(result)
        except ValueError as e:
            s.append(int(e))
        except (TypeError):
            print("wrong type")
            s.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            s.append(0)
        except (IndexError):
            print("out of range")
            s.append(0)
        finally:
            pass

    return s
