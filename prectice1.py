def unique_in_order(iterable):
    my_ = ""
    for letter in iterable:
        my_ += letter + " "
    my_ = my_.split()
    print(my_)

unique_in_order("AABBAA")
