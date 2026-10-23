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
    # Why do those indexes work? The index starts at 4 and stops before index 6. The starting is index is included, but the ending index is excluded.

    print(my_list[4:])
    # What do you notice? That the index starts at the fourth index and continues to the end.
    #Is the result the same as above? Yes.

    print(my_list[-2:])
    # What does this do? It returns the last two elements
    # Why is it useful? Negative indexing lets you access items frm the end of a list without needing to know the length

    my_list.remove("l")
    print(my_list)
    # What changed? The "l" got removed 
    # Where did it remove the "l" from? it removed the first l it incountered leading the following l which was orginally at index 3 be shifted to index 2 after the first one being removed.

    my_list.insert(2, "l")
    print(my_list)
    # Did it go where you expected? What is at index 2 now? I expected it to go to index 2 and shift the other elements.
    
    
    del my_list[0]
    print(my_list)
    # What item got removed? "h"

    last_item = my_list.pop()
    print(last_item)
    print(my_list)
    # What item was removed? What’s left in the list? "!", now only ['e', 'l', 'l', 'o'] is left in the list

    print(my_list[2])
    # What is it? It is the element at index 2 which is "l"

    print("!" in my_list)
    # True or False? Why? False, because we removed it and it is no longer in our list


    my_list.sort(reverse=True)
    print(my_list)
    # What is the new order?  The letters are sorted in reverse ALPHABETICAL order.
    # Did sort() return anything? The sort() method only changes the orgininal list.
    
    print(sorted(my_list))
    print(my_list)
    # Did the original change? No because sorted creates and return a new list without having to affect the orginally one.
    # What’s the difference between sorted() and sort()? 
        #sort() changes the og list
        #sorted() returns a new sorted list and preserves the orginal. 

#PART B: TUPLES
    my_tuple = ("red", "green", "blue")
    print(my_tuple)
    # What values are inside this tuple? "red", "green", "blue"


    print(my_tuple[0])
    print(my_tuple[-1])
    # What was printed in each case? Why does negative indexing work? 
    # print(my_tuple[0]) returns "red"
    #print(my_tuple[-1]) return "blue" and works because is counting starting from the end

    #my_tuple[1] = "yellow"
    # What happens? Error because you cannot change the element after they are created
    # What error do you get? TypeError: 'tuple' object does not support item assignment

    one_item = ("hello",)
    print(one_item)
    # What do you notice about the syntax? I noticed that the comma was necessary to create a tuple with only one item. If there is no comma, Pythons treats the value as a string.

    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
    # How many "red" entries are there? 3

    print(colors.index("green"))
    # What position is "green" in the tuple? Index 3

#PART C: SETS

    my_set = {"apple", "banana", "cherry"}
    print(my_set)
    #Does the order match what you typed? Why or why not? NO because sets do not keep items in the specfic order you typed it in.

    my_set.add("orange")
    print(my_set)
    # What changed? Organge was apply to be added

    my_set.add("banana")
    print(my_set)
    # Did anything change? Why or why not? No, nothing change because "banana" was already in the set, and sets do not store duplicate values.

    my_set.remove("apple")
    print(my_set)
    # Which item is gone? apple was removed

    my_set.discard("pear")
    # What happened? Was there an error? Nothing changed, but it did not fufil what we asked it to do because it was never in the set.

    tropical = {"banana", "mango", "papaya"}
    all_fruits = my_set.union(tropical)
    print(all_fruits)
    # What items are in the result? {'cherry', 'banana', 'papaya', 'mango', 'orange'}
    # Any duplicates? No duplicates but "banana" appears in both sets.


#PART D: Dictionaries
    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}
    print(my_dict)
    # What keys and values are present?
    #Keys: "name", "age", "grade"
    #Value: "Sam", 16, "11th"

    print(my_dict["age"])
    # What value did this return? 16

    #print(my_dict["school"])
    # What error do you get? KeyError: 'school' because "school" is not yet a key in dictionary

    my_dict["grade"] = "12th"
    print(my_dict)
    # Did the value update? Yes. The value for "grade" changed from "12th" while the key stayed the same.

    my_dict["school"] = "Central High"
    print(my_dict)
    # What’s the new key and value?
    #Key: "school"
    #Value: "Central High"

    del my_dict["age"]
    print(my_dict)
    # Which key is missing now? the key "age" was deleted which lead the value 16 to go as well

    print(my_dict.get("locker"))
    # What value was returned? None.
    #  Was there an error? No error but the .get() method return none as default because it doesn't exist

    for key, value in my_dict.items():
        print(key, "->", value)
    # What got printed?
    #name -> Sam
    #grade -> 12th
    #school -> Central High
    # How does this help you read the dictionary? It shows us the key-value pair key first and value second and the loop is helpful to read because it prints each pair on a seperate line.








if __name__ == "__main__":
    main()
