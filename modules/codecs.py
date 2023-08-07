from codecs import open

text = open('text.txt', 'a', 'utf-8')

print('ążćęółź', file=text)

text.close()