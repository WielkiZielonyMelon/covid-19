import matplotlib.pyplot as plt
import numpy as np

def plot_data(x_labels, y_infections, y_deaths, timestamp,
              vovoidships_previous_data=None, previous_timestamp=None):
    fig, ax = plt.subplots()
    width = 0.25
    x_values = np.arange(len(x_labels))
    y_infections = [x[1] for x in y_infections]
    infections = ax.bar(x_values, y_infections, width, label="Infekcje")
    y_deaths = [x[1] for x in y_deaths]
    deaths = ax.bar(x_values + width, y_deaths, width, label="Zgony")
    if vovoidships_previous_data:
        previous = ax.bar(x_values - width, vovoidships_previous_data, width, label="Poprzednie infekcje i zgony")
    
    ax.set_ylabel("Liczba infekcji/zgonów")
    if previous_timestamp:
        ax.set_title("Porównanie liczby infekcji/zgonów na województwo/powiat z " + previous_timestamp + " i " + timestamp)
    else:
        ax.set_title("Liczba infekcji/zgonów na województwo/powiat " + timestamp)
    
    ax.set_xticks(x_values)
    ax.set_xticklabels(x_labels, rotation="vertical")
    
    ax.legend()
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    
    autolabel(infections)
    autolabel(deaths)
    if vovoidships_previous_data:
        autolabel(previous)
    
    plt.show()
