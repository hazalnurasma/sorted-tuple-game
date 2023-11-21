# keeping colors in a dict
color_dict = {
    "pm": 1,
    "ay": 2,
    "sr": 3,
    "kr": 4,
    "kv": 5,
    "gr": 6,
    "mo": 7,
    "yy": 8,
    "ky": 9,
    "lc": 10,
    "mv": 11,
    "tt": 12
}

# keeping tubes in a dict
tube_dict = {
    "tup_1": ["pm", "ay", "sr", "kr"],
    "tup_2": ["kv", "gr", "mo", "yy"],
    "tup_3": ["mo", "kr", "ky", "sr"],
    "tup_4": ["lc", "mv", "kv", "sr"],
    "tup_5": ["ay", "kr", "lc", "ky"],
    "tup_6": ["gr", "kr", "yy", "tt"],
    "tup_7": ["gr", "lc", "pm", "mo"],
    "tup_8": ["ky", "tt", "yy", "kv"],
    "tup_9": ["ay", "lc", "yy", "kv"],
    "tup_10": ["ky", "ay", "tt", "pm"],
    "tup_11": ["gr", "mv", "sr", "pm"],
    "tup_12": ["mv", "mv", "tt", "mo"],
    "tup_13": [],  # boş tüp
    "tup_14": []   # boş tüp
}

# create categories for each tube
category_lists = []

# categorize tubes
for tube_name, tube in tube_dict.items():
    category_list = []
    for color in tube:
        category_list.append(color_dict[color])
    category_lists.append(category_list)

# seperating variables to according tuples
result_dict = {}
for category_list in category_lists:
    for i, color_type in enumerate(category_list, start=1):
        if color_type not in result_dict:
            result_dict[color_type] = [f"clr_{color_type}_{i}"]
        else:
            result_dict[color_type].append(f"clr_{color_type}_{i}")



# tuples for each color variable (one to four)
#final_tubes = list(result_dict.values()) + [empty_tubes]
final_tubes = [result_dict.get(i, []) for i in range(1, 13)]

# empty tuples
final_tubes.append([[] for _ in range(4)])
final_tubes.append([[] for _ in range(4)])
#empty_tube_count = 2
#empty_tubes = [[] for _ in range(empty_tube_count)]

# adding empty tuples
"""
for i in range(empty_tube_count):
    final_tubes.append([[] for _ in range(4)])
"""



# the result
for i, final_tube in enumerate(final_tubes, start=1):
    print(f"Tup_{i}: {final_tube}")

