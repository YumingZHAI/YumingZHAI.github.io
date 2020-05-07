import sys, re, codecs

FR = sys.argv[1]
ZH = sys.argv[2]

listSeg = []
TPs = []
fType = []

with codecs.open(FR, encoding="utf-8") as Fpairs :
        for line in Fpairs :
                line = line.strip('\n')
                m = re.match(r'(\d+ - .*?) \# (.*?) \# (.*?)$', line)
                segF = m.group(1)
                # TP : translation and type 
                TP = m.group(2)
                label = m.group(3)

                listSeg.append(segF)
                TPs.append(TP)
                fType.append(label)

zListSeg = []
zTPs = []
zType = []

with codecs.open(ZH, encoding="utf-8") as Zpairs :
        for line in Zpairs :
                line = line.strip('\n')
                m = re.match(r'(\d+ - .*?) \# (.*?) \# (.*?)$', line)
                segZ = m.group(1)
                # TP : translation and type 
                TP = m.group(2)
                label = m.group(3)
                zListSeg.append(segZ)
                zTPs.append(TP)
                zType.append(label)

# if english segment in FR list is also in ZH list 
for segment in listSeg:
        if segment in zListSeg:
                zIndice = zListSeg.index(segment)
                fIndice = listSeg.index(segment)
                fLabel = fType[fIndice]
                zLabel = zType[zIndice]
                #print segment + " | F: " + fLabel + " | Z: " + zLabel
                if fLabel != zLabel:
                        print segment + " | F: " + fLabel + " | Z: " + zLabel

