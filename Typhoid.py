def typhoid():
    count = 0
    for i in symp:
        if i == '3':
            temp = float(input('Enter your body temperature:  '))
            if temp>=99:
                count += 1
        if i == '4':
            count += 1
        if i == '17':
            count += 1
        if i == '18':
            count += 1

    if count >= 3:
        print('You have been diagnosed with TYPHOID')
        print('Medications :\n Maintain fluid diet\n Anti-Biotics\n Penicillin')
