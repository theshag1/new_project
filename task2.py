with open('pupilation_country') as f:
    data = f.readlines()
    for i in range(1, len(data)):
        line = data[i]
        if line.split(',')[2].split('"')[0]>200000:
