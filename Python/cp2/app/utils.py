def get_population():
    keys = ['col', 'mex', 'bra', 'arg', 'per', 'chi', 'ecu', 'bol', 'uru', 'par']
    values = [300, 500, 700, 900, 100, 200, 400, 600, 800, 1000]
    return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
