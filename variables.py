colors = ["pm", "ay", "sr", "kr", "kv", "gr", "mo", "yy", "ky", "lc", "mv", "tt"]

# color variables defined
clr_1="pm"
clr_2="ay"
clr_3="sr"
clr_4="kr"
clr_5="kv"
clr_6="gr"
clr_7="mo"
clr_8="yy"
clr_9="ky"
clr_10="lc"
clr_11="mv"
clr_12="tt"

# Tubes were defined by reference to the .txt file
tup_1 = ["pm", "ay", "sr", "kr"]
tup_2 = ["kv", "gr", "mo", "yy"]
tup_3 = ["mo", "kr", "ky", "sr"]
tup_4 = ["lc", "mv", "kv", "sr"]
tup_5 = ["ay", "kr", "lc", "ky"]
tup_6 = ["gr", "kr", "yy", "tt"]
tup_7 = ["gr", "lc", "pm", "mo"]
tup_8 = ["ky", "tt", "yy", "kv"]
tup_9 = ["ay", "lc", "yy", "kv"]
tup_10 = ["ky", "ay", "tt", "pm"]
tup_11 = ["gr", "mv", "sr", "pm"]
tup_12 = ["mv", "mv", "tt", "mo"]
tup_13 = []  # empty tuple
tup_14 = []  # empty tuple

tuples = [tup_1, tup_2, tup_3, tup_4, tup_5, tup_6, tup_7, tup_8, tup_9, tup_10, tup_11, tup_12, tup_13, tup_14]

for i, tup in enumerate(tuples):
    if not tup:
        print(f"Tüp {i + 1}: Boş")
    else:
        print(f"Tüp {i + 1}: {', '.join(tup)}")
