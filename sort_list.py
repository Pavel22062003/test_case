from enum import Enum


class SortType(Enum):
    INCREASE = False
    DECREASE = True


def sort_list(data: list, sort_type: SortType):
    data.sort(reverse=sort_type.value)
    return data

#Exmpale
# test = ['1', '23', '6789', '1']
# print(sort_list(test, sort_type=SortType.INCREASE))
# print(sort_list(test, sort_type=SortType.DECREASE))

