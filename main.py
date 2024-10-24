def encode(phone):
    #Personal Email account 
    encoded_string = ''
    int_list = [int(char) for char in phone]

    for i in range(len(int_list)):
        int_list[i] += 3
        encoded_string += str(int_list[i])

    return encoded_string

def decode(encoded_string):
    #UF Email Accou 
    new_decoded_str = ''
    num_list = [int(char) for char in encoded_string]

    for i in range(len(num_list)):
        num_list[i] -= 3
        new_decoded_str += str(num_list[i])

    return new_decoded_str


if __name__ == "__main__":
    is_running = True

    while is_running:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        operation = input("Please enter an option: ")

        if operation == "1":
            num_string = str(input("please enter your password to encode: "))
            ans = encode(num_string)
            print("Your password has been encoded and stored!")
       	elif operation == '2':
            dans = decode(encode(num_string))
            print("The encoded password is: " + ans + ", and the original password is: " + dans)
        else:
            is_running = False
