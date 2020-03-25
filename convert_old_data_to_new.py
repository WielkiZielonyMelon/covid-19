import codecs
import glob
import json
import os

import common

OLD_FILES_PATH = os.path.join("data", "old_format", "*")

def grab_files():
    return glob.glob(OLD_FILES_PATH)

for file_path in grab_files():
    with open(file_path) as json_file:
        print("Analyzing file {}".format(file_path))
        data = json.load(json_file)
        vovoidships_infections_and_deaths = {}
        for d in data:
            vovoidship = d[common.VOVOIDSHIP]
            infections = int(d[common.INFECTIONS] or 0)
            deaths = int(d[common.DEATHS] or 0)
            if vovoidship in vovoidships_infections_and_deaths:
                infections = vovoidships_infections_and_deaths[vovoidship][0] + infections
                deaths = vovoidships_infections_and_deaths[vovoidship][1] + deaths

            vovoidships_infections_and_deaths[vovoidship] = (infections, deaths)

        if not common.WHOLE_POLAND in vovoidships_infections_and_deaths:
            infections = 0
            deaths = 0
            for _, infections_and_deaths in vovoidships_infections_and_deaths.items():
                infections += infections_and_deaths[0]
                deaths += infections_and_deaths[0]

            vovoidships_infections_and_deaths[common.WHOLE_POLAND] = (infections, deaths)

        for vovoidship in common.VOVOIDSHIPS:
            if not vovoidship in vovoidships_infections_and_deaths:
                vovoidships_infections_and_deaths[vovoidship] = (0, 0)

        converted_data = []
        for vovoidship, infections_and_deaths in vovoidships_infections_and_deaths.items():
            converted_data.append({common.VOVOIDSHIP: vovoidship,
                common.INFECTIONS: infections_and_deaths[0],
                common.DEATHS: infections_and_deaths[1]})

        target_file = os.path.basename(file_path)
        target_file = os.path.join(common.DEFAULT_DATA_DIRECTORY, target_file)
        print("Saving to {}".format(target_file))
        with codecs.open(target_file, 'w', 'utf-8') as target_json_file:
            json.dump(converted_data, target_json_file, ensure_ascii=False)

