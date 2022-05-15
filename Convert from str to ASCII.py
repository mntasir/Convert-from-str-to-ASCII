class convIntoASCII:
    def convert(self,name):

        ascii = ''
        posi1 = ''
        for i in range(33, 126):
            ascii += chr(i)

        for x in name:
            pos = ascii.find(x)
            pos += 33
            posi = str(pos)
            posi1 += posi
        return posi1
    #print(posi1)

name = input('enter your name to convert it to ASCII num\n')
nam = convIntoASCII()
e = nam.convert(name)
print(e)