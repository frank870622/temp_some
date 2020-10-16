import sys, wget, tarfile, os
input_year = input('input year')
input_month = input('input month')

for i  in range(1, 31):
    url = ''
    out_fname = ''
    if i < 10:
        url = 'http://data.ris.ripe.net/rrc00/' + input_year + '.' + input_month + '/updates.' + input_year + input_month + '0' + str(i) + '.1200.gz'
        out_fname = input_year + input_month + '0' + str(i) + '.gz'

    else:
        url = 'http://data.ris.ripe.net/rrc00/' + input_year + '.' + input_month + '/updates.' + input_year + input_month + str(i) + '.1200.gz'
        out_fname = input_year + input_month + str(i) + '.gz'
    
    wget.download(url, out=out_fname)
    #tar = tarfile.open(out_fname)
    #tar.extractall()
    #tar.close()
    #os.remove(out_fname)