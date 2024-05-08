from lazy_streams import stream

# lazy_streams
# pystreamapi https://github.com/PickwickSoft/pystreamapi

names = ['Bob', 'Sally', 'Jane', 'Joe', 'Emily', 'Jake', 'John']

filterdNames = stream(names) \
    .filter(lambda x: len(x) > 3) \
    .sort() \
    .map(lambda x: "First name: %s" % x) \
    .to_string("\n")

newList = stream(names).take(2).to_list()

st = stream(names).filter(lambda x: x == 'Bob').to_list()[0]


'''

flatten() - Will flatten a list-of-lists to a flat list.
sort(key=None, reverse=False) - Will return a sorted Stream using the given key. If reverse is true, will reverse the sort.
map(func) - Will call func on each item of the stream's list and return the result.
filter(func) - Will call func on each item of the stream's list and only keep the ones where func reutrns True.
reverse() - Will simply reverse the order of the items. This operation does not perform any sorting. It simply mirrors the values.

'''


def search_el_in_the_list(elements_list, search_T):
    return stream(elements_list).filter(lambda x: x == search_T).to_list()


def get_first_el_from_filtered_list(elements_list, search_T):
    return stream(elements_list).filter(lambda x: x == search_T).to_list()[0]


# TODO To test, try map()
names = search_el_in_the_list(names, 'Bob')

