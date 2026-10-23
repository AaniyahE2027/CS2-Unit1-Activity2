def main():

    my_list = ["h", "e", "l", "l", "o"]
    print(my_list)
    # What do you see? ['h', 'e', 'l', 'l', 'o']
    my_list.append("!")
    print(my_list)
    # What changed? Describe the difference between the original and updated list: It added '!' to the add of the code.

    print(len(my_list))
    # How many elements are there? Record it: 6
    print(my_list[4:6])
    # What values were returned? It's returning ['o', '!']
    # Why do those indexes work? Pick the first and the last idexes but does not include the last
    print(my_list[4:])
    # What do you notice? That the index starts at the fourth index and continues to the end.
    #Is the result the same as above? Yes.
    print(my_list[-2:])
    # What does this do? 
    # Why is it useful?
    my_list.remove("l")
    print(my_list)
    # What changed? The "l" got removed from 
    # Where did it remove the "l" from?
    my_list.insert(2, "l")
    print(my_list)
# Did it go where you expected? What is at index 2 now?
    del my_list[0]
    print(my_list)
# What item got removed?
    last_item = my_list.pop()
    print(last_item)
    print(my_list)
# What item was removed? What’s left in the list?
    print(my_list[2])
# What is it?
    print("!" in my_list)
# True or False? Why?
    my_list.sort(reverse=True)
    print(my_list)
# What is the new order? Did sort() return anything?
    print(sorted(my_list))
    print(my_list)
# Did the original change? What’s the difference between sorted() and sort()?

#PART B: TUPLES
    my_tuple = ("red", "green", "blue")
    print(my_tuple)
# What values are inside this tuple?

    print(my_tuple[0])
    print(my_tuple[-1])
# What was printed in each case? Why does negative indexing work?

    #my_tuple[1] = "yellow"
# What happens? What error do you get?

    one_item = ("hello",)
    print(one_item)
# What do you notice about the syntax?

    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
# How many "red" entries are there?

    print(colors.index("green"))
# What position is "green" in the tuple?

#PART C: SETS

    my_set = {"apple", "banana", "cherry"}
    print(my_set)
# Does the order match what you typed? Why or why not?

    my_set.add("orange")
    print(my_set)
# What changed?

    my_set.add("banana")
    print(my_set)
# Did anything change? Why or why not?

    my_set.remove("apple")
    print(my_set)
# Which item is gone?

    my_set.discard("pear")
# What happened? Was there an error?

    tropical = {"banana", "mango", "papaya"}
    all_fruits = my_set.union(tropical)
    print(all_fruits)
# What items are in the result? Any duplicates?

#PART D: Dictionaries
    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}
    print(my_dict)
# What keys and values are present?

    print(my_dict["age"])
# What value did this return?

    #print(my_dict["school"])
# What error do you get?

    my_dict["grade"] = "12th"
    print(my_dict)
# Did the value update?

    my_dict["school"] = "Central High"
    print(my_dict)
# What’s the new key and value?

    del my_dict["age"]
    print(my_dict)
# Which key is missing now?

    print(my_dict.get("locker"))
# What value was returned? Was there an error?

    for key, value in my_dict.items():
        print(key, "->", value)
# What got printed? How does this help you read the dictionary?








if __name__ == "__main__":
    main()
