import json, os

# Filtering worldwide cities to get relevant NE Scotland ones
# List from here http://bulk.openweathermap.org/sample/
# So that we can run this api.openweathermap.org/data/2.5/weather?id=2172797 to get local weather


file_path = "reference_data/"
target_file = "city.list.json"


def load_data():
    base_folder = os.path.dirname(__file__)
    file_p = os.path.join(base_folder, 'data', 'reference_data', 'city.list.json')
    with open(file_p, 'r') as fp:
        city_dict = json.load(fp)
    return city_dict


def filter_NE_only(city_list):
    short_list = []

    for city in city_list:
        GB = False
        NS = False
        EW = False
        for key, val in city.items(): #outer dictionary
            if key == "country" and val == "GB":
                GB = True # we are only interested in GB places (no point testing lat long of whole world)
            if key == "coord":
                for k, v in val.items(): #inner dictionary
                    # equivalent of our bounding box
                    if k == "lon" and float(v) > -2.78633 and float(v) < 1.9112:
                        EW = True
                    if k == "lat" and float(v) > 56.955 and float(v) < 57.6875:
                        NS = True
            if GB and NS and EW:
                short_list.append(city)
    return short_list


def write_out(in_list):
    base_folder = os.path.dirname(__file__)
    out_p = os.path.join(base_folder, 'data', 'reference_data', 'ne_towns.json')
    with open(out_p, 'w') as json_file:
        json.dump(in_list, json_file, indent = 4)


def main():
    city_data = load_data()
    ne_locations = filter_NE_only(city_data)
    write_out(ne_locations)


if __name__ == '__main__':
    main()
