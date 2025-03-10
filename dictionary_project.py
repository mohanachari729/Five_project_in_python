dictionary_m = {}
while True :
    print("\n Dictionary Management Sysyem")
    print("1. Add a word")
    print("2. Search for meaning")
    print("3. display all thw words")
    print("4.update meaning")
    print("5. delete word")
    print("6. Exit")

    choice = input("enter the choice :")

    if choice == "1" :
        word = input("enter the word :")
        meaning = input("enter the meaning :")
        print(word and meaning)
        dictionary_m[word] = meaning
        print(dictionary_m)
        print("word added successfully!")
    elif choice == "2" :
        meaning_1 = input("search for meaning :")
        print(f"the meaning of {meaning_1} is {meaning}")
    elif choice == "3" :
        print(dictionary_m)
    elif choice == "4" :
        update_1 = input("update meaning of the word :")
        meaning_2 =input ("update meaning :")
        dictionary_m[update_1] = meaning_2
        print(dictionary_m)
    elif choice == "5" :
        word = input('enter the deleted words :')
        print(word)
        dictionary_m.pop(word)
        print(dictionary_m)
        print("the word deleted successfully!")
    elif choice == "6" :
        print("exiting from the dictionary")
        break


        
