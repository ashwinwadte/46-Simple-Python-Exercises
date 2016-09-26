'''
Write a program that given a text file will create a new text file
in which all the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file).
'''

def re_arranger(file_name):
    old_file = open(file_name,'r')
    arranged_file = open('arranged.txt','w')
    count = 1

    for i in old_file:
        arranged_file.write(str(count) +' ' + i + '\n')
        count += 1
    old_file.close()
    arranged_file.close()

re_arranger('palindromes.txt')