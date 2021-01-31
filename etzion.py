import requests


def download_and_convert(url, outfilename):
    webpage = requests.get(url).text
    with open(outfilename, 'w') as ofile:
        i = 0
        for ch in webpage:
            if ch != '\n':
                i += 1
            if ch == '1':
                ofile.write(str(i) + " ")
        print("Final i", i)



download_and_convert('https://web.archive.org/web/20021007171013/http://saturn.hut.fi/~pat/codcol/color13.html', 'a265032_1zc.1024.initial')
download_and_convert('https://web.archive.org/web/20021007171013/http://saturn.hut.fi/~pat/codcol/color14.html', 'a265032_1zc.2048.initial')
