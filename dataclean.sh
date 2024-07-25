sed "s/[():!\.,';?\"\n]/ /g" $1 > output_file2.txt
sed  's/^[0-9]*[[:space:]]*//g' output_file2.txt > output_file3.txt
./word_list.py 
sort output_list.lst >  sorted_list

