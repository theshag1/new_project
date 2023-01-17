def get_popilation():
    import csv

    with open('world_pupile.csv') as f:
        lines = f.readlines()
        result = []
    for line in lines:
        try:
            name, count = line.split(',')[0].strip(), int(line.split(',')[2].strip())
        except ValueError as e:
            print(e)
        else:
            if count > 20000000:
                result.append(f"{name} : {count}")
    return result

