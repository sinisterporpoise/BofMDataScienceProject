# BofMDataScienceProject
A collection of files and a Jupyter Notebook for a simple data science project on the Book of Mormon

The preliminary part of this program has been doing the data cleaning of the 1830s Book of Mormon text, and generating the CSV files necessary for analysis.  The intent is to use the K Nereest Neighbor Alorithm to see if all the Books of Mormon more than likely have the same author or a different author.  This could serve as a starting point for people who want to do more robust research later.

## Excluded Books

For now, 2nd Nephi, 4th Nephi, and Words of Mormon have been excluded. The testimonies of the 3 witnesses and the testimonies of the 8 witnesses have also been excluded, because they are known to have different authors.

## Reason for Choosing the 1830 Edition

The 1830 Edition is the one that is closest to what Joseph Smith actually wrote down, as the Church of Jesus Christ of Latter Day Saints has edited the Book of Mormon hundreds of times in the intervening years. Chapter headings have been removed.

## Source for the Material

The text for the 1830 Book of Mormon was obtained from Wikisources.   

# Gencsv.py

This is a Python script designed to go through the list files, count the occurrences of each word, divide the occurences by the total, and then output the word and its frequency to a CSV file format that can easily be read by the Pandas data library.

## Datacleaning Process

The data cleaning process used three seprate shell scripts and could have been done more efficiently. The first shell script removed punctuation from the tests, the second script, word_list.py, separated all the text and into words and printed the word out line by line. The third script, listgen.sh sorted the words in the script into final output. The final result, sorted_file was then moved into the wordlist file for further process. Finally, cleanup.sh removed the excess files generated.
