import utils

data = [
    {'Country': 'Colombia', 'Population': 50},
    {'Country': 'Argentina', 'Population': 100},
    {'Country': 'Peru', 'Population': 30},
    {'Country': 'Chile', 'Population': 40},
    {'Country': 'Ecuador', 'Population': 20},
    {'Country': 'Bolivia', 'Population': 60},
    {'Country': 'Uruguay', 'Population': 80},
    {'Country': 'Paraguay', 'Population': 10},
    {'Country': 'Venezuela', 'Population': 70},
    {'Country': 'Brasil', 'Population': 90},
    {'Country': 'Mexico', 'Population': 5},
]

def run():
    keys, values = utils.get_population()
    print(keys)
    print(values)
    print(keys, values)

    country = input('Type Country => ')
    country = country.capitalize()

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()