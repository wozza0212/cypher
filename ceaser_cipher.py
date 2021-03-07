
# Sample messages
# mjqqtbymjwj 5
# 8x4fj1nfjfl4w3 9

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '£', '€', '$']


def encoder():
    print('Welcome to the simple encoder, all you have to do is type a message,'
          'and then a shift number to encode it')

    message = input('Please enter the message that you would like encoding:').lower()
    shift_number = int(input('Now please enter your shift number, make sure you write this down or'
                             'remember it'))

    index_list = []
    new_index = []
    new_message = ''

    for i in message:
        index_list.append(alphabet.index(i))
        for x in index_list:
            new_num = x + shift_number
            if new_num > len(alphabet):
                new_num -= len(alphabet)
        new_index.append(new_num)
    for x in new_index:
        new_message += alphabet[x]
    return new_message


def decoder():
    print('This is the decoder, enter your coded message and your shift number, and we\'ll decode your message')
    coded_message = input('Please enter your coded message here:')
    unshift_number = int(input('Please enter the shift number your used last time here!'))

    index_list = []
    old_index = []
    old_message = ''
    for x in coded_message:
        index_list.append(alphabet.index(x))
        for i in index_list:
            old_num = i - unshift_number
            if old_num < 0:
                old_num += len(alphabet)
        old_index.append(old_num)

    for x in old_index:
        old_message += alphabet[x]
    return old_message


print('Welcome to the cypher!!')
running = True
while running:
    choice = input('Would you like to use the encoder or the decrypter program?,'
                   ' enter \'e\' or \'d\', or enter \'q\' to quit!')
    if choice == 'e':
        print(encoder())
    elif choice == 'd':
        print(decoder())
    elif choice == 'q':
        running = False
    else:
        print('Incorrect entry, please read the instructions')
print('Goodbye')


