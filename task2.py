with open('pupilation_country') as f:
    data = f.readlines()
    for i in range(1, len(data)):
        line = data[i]
        people =  line.split(',')[2].split('"')[0]
        people = int(people)
        print(type(people))
