import os

input_year = input('input year')
input_month = input('input month')
for i  in range(1, 31):
    cmd_text = ''
    if i < 10:
        cmd_text = 'bgpreader -d singlefile -o upd-file=' + input_year + input_month + '0' + str(i) + ' > output' + '0' + str(i)+  '.txt'
    else:   
        cmd_text = 'bgpreader -d singlefile -o upd-file=' + input_year + input_month + str(i) + ' > output' + str(i)+  '.txt'
    print(cmd_text)
    print(os.system(cmd_text))
