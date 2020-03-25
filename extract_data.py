import json

import common

def extract_data_from(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        x_labels = []
        y_infections_per_vovoidship = []
        y_deaths_per_vovoidship = []
        for item in data:
            vovoidship = item[common.VOVOIDSHIP]
            vovoidship = vovoidship.replace("-", "-\n", 1)
            x_labels.append(vovoidship)
            y_infections_per_vovoidship.append((vovoidship, int(item[common.INFECTIONS] or 0)))
            y_deaths_per_vovoidship.append((vovoidship, int(item[common.DEATHS] or 0)))

    start_of_date = filename.find(common.DATA_FILENAME_HEADER) + \
            len(common.DATA_FILENAME_HEADER)
    timestamp = filename[start_of_date:-(len(common.DATA_FILENAME_EXT) + 1)]
    x_labels.sort()
    y_infections_per_vovoidship.sort()
    y_deaths_per_vovoidship.sort()

    return x_labels, y_infections_per_vovoidship, y_deaths_per_vovoidship, timestamp

