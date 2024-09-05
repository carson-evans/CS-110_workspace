# A comparable data type that represents a country by its name, capital, and population.

import stdarray
import stdio


class Country:
    # Constructs a country given its name, capital, and population.
    def __init__(self, name, capital, population):
        self._name = name  # name
        self._capital = capital  # capital city
        self._population = population  # population

    # Returns True if this country is less than the other country by name, and False otherwise.
    def __lt__(self, other):
        return self._name < other._name

    # Returns True if this and the other country have the same name, and False otherwise.
    def __eq__(self, other):
        return self._name == other._name

    # Returns a string representation of this country.
    def __str__(self):
        return self._name + " (" + self._capital + "): " + str(self._population)


# Unit tests the data type.
def _main():
    countries = stdarray.create1D(5, None)
    countries[0] = Country("Brazil", "Brasilia", 218689757)
    countries[1] = Country("Russia", "Moscow", 141698923)
    countries[2] = Country("India", "New Delhi", 1425775850)
    countries[3] = Country("China", "Beijing", 1409670000)
    countries[4] = Country("South Africa", "Cape Town", 58048332)
    stdio.writeln("Unsorted:")
    for country in countries:
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln("Sorted by name:")
    for country in sorted(countries):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln("Sorted by capital:")
    for country in sorted(countries, key=lambda x: x._capital):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln("Sorted by population:")
    for country in sorted(countries, key=lambda x: x._population):
        stdio.writeln(country)
    stdio.writeln()
    stdio.writeln("Reverse sorted by population:")
    for country in sorted(countries, key=lambda x: x._population, reverse=True):
        stdio.writeln(country)


if __name__ == "__main__":
    _main()
