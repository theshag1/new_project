import csv
def get_gdp():
    with open('world.txt') as f:
        lines = csv.DictReader(f)
        print(lines)
        lst = []
        for line in lines:
            try:
                int(line.get("GDP ($ per capita)"))
            except ValueError as e:
                print(e)
            else:
                if int(line.get("GDP ($ per capita)")) > 1000:
                    lst.append(f"{line.get('Country')}, {line.get('GDP ($ per capita)')}")

    return lst
print(get_gdp())
