import sys

from extract_data import extract_data_from
from plot_data import plot_data

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x_labels, y_infections, y_deaths, timestamp = extract_data_from(sys.argv[1])
        plot_data(x_labels, y_infections, y_deaths, timestamp)
    elif len(sys.argv) == 3:
        x_labels, y_infections, y_deaths, previous_timestamp = extract_data_from(sys.argv[1])
        infections = [x[1] for x in y_infections]
        deaths = [x[1] for x in y_deaths]
        vovoidships_previous_data = [sum(x) for x in zip(infections, deaths)]

        x_labels, y_infections, y_deaths, timestamp = extract_data_from(sys.argv[2])
        plot_data(x_labels, y_infections, y_deaths, timestamp, vovoidships_previous_data, previous_timestamp)
    else:
        print("Provide path to data!")


