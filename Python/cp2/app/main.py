import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv')
    country = input('Type Country => ')
    country = country.capitalize()

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
        charts.generate_line_chart(labels, values)

    else:
        print('No se encontro el pais')

if __name__ == '__main__':
    run()