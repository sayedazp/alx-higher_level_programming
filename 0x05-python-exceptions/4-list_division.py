#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for y in range(list_length):
        try:
            div = my_list_1[y]/my_list_2[y]
        except IndexError:
            print("{}".format("out of range"))
            break
        except (ValueError, TypeError):
            div = 0
            print("{}".format("wrong type"))
            continue
        except ZeroDivisionError:
            div = 0
            print("{}".format("division by 0"))
        finally:
            new_list.append(div)
    return new_list
