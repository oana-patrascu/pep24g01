def putere():
    result = None
    while True:
        user_data1 = input('Numar1:')
        if user_data1 in ['Q','q']:
            return result
        num1 = int(user_data1)
        num2 = int(input('Numar2:'))
        result = num1 **num2
print(putere())
