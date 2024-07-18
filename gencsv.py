#!/usr/bin/env python3

#---------------------
# Remaining Books
#--------------------
books = ["1stNephi", "3rdNephi", "Alma", "Ether", "Enos", "Helaman", "Jacob", "Jarom", "Mormon","Moroni", "Mosiah", "Omni", "Usher"]
# Don't you hate it when you realize you could have made this easier on yourself?

for book in books:
    data = ""
    data_2 = []
    # Open the file as a list, read in the file and then split it into an area
    with open(f'{book}.lst','r') as f:
        data = f.read()

    # Make sure we get the  length of the total to calculate word frequency.)
    data_2 = data.split('\n')
    total = len(data_2) + 1


    # Declare some variables we will need.
    frequency = 0.0
    tmp_list = []
    prev_word = data_2[0]
    current_word = data_2[0]
    counter = 0


    # Prime the Csv file
    tmp_list.append(("Word", "Frequency"))


    for item in data_2:
        if len(item) < 4 or len(item) > 8:
            continue
        else:
            current_word = item;
            counter += 1
            if (current_word == prev_word):
                continue
            prev_word = item
            frequency = counter/total
            tmp_list.append((item, frequency))
            prev_word = ""
            prev_word = current_word
            current_word = ""
            counter = 0

    with open(f'{book}.csv', 'w') as f:
        tmp_array = []
        for item in tmp_list:
            tmp_array.append(item)
            f.write(f"{tmp_array[0][0]},{tmp_array[0][1]}\n")
            tmp_array = []


