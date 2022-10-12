import pprint

data = {
    "len": 25.4,
    "wi": 16.2,
    "he": 33.7,
}

data_reformat = {
    "length": round(data["len"]),
    "width": str(data["wi"]),
    "height": round(data["he"]),
}

pprint.pprint(data_reformat)
