def encoder(not_encoded):
    result = []
    final = ""
    for i in not_encoded:
        result.append(int(i))
    for i in result:
        j = i + 3
        #add 3 to the different values in the string
        final += str(j)
    return final

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded_number = input("Please enter your password to encode: ")
            decoded_number = encoder(encoded_number)
            #creates a decoded number
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            print("The encoded password is " + str(decoded_number) + " and the original password is " + str(encoded_number) + ".")
            print()
        elif option == 3:
            break

if __name__ == '__main__':
    main()
