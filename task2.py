with open('pupilation_country' , 'r') as f:
    data = f.readlines()
    contry_name = []
    for i in range( 1, len(data)):
        line = data[i]
        print(line.split( ', ')[0].split('"')[1])
        contry_name.append(line.split(",")[0])