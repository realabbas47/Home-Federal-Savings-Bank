greatings = input('Greatings: ').lower().replace(' ', '')

if greatings[0:5] == 'hello':
    print('$0')
elif greatings[0] == 'h':
    print('$20')
else:
    print('$100')
