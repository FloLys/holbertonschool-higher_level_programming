#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            div_list.append(div)
            continue
        except ZeroDivisionError:
            div_list.append(0)
            print("division by 0")
            continue
        except (TypeError, ValueError):
            div_list.append(0)
            print("wrong type")
            continue
        except IndexError:
            div_list.append(0)
            print("out of range")
            continue
        finally:
            continue
    return div_list
