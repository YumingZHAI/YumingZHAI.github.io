# if target lgg is ZH, 2nd arg is "zh", else it's "x" 
 
import sys, re 

FILE = sys.argv[1]
zh = sys.argv[2]

if zh == "x":
	flag = False
elif zh == "zh": 
	flag = True 

nb_en = 0 
nb_trad = 0

if FILE.endswith("txt"):
	with open(FILE) as pairs:
		for line in pairs:
			line = line.strip('\n')
			m = re.match(r'\d+ - (.*) \# (.*) \# .*$', line)
			source = m.group(1) 
			target = m.group(2)

			nb_src = len(source.split()) 
			print(source + " " + str(len(source.split())))
			## count Chinese characters in string 
			## under python3, don't need to string.decode('utf8') for chinese string 
			if flag == True:
				nb_tgt = len(target.replace(' ',''))
				print(target + " " + str(nb_tgt))
			else:
				nb_tgt = len(target.split()) 
				print(target + " " + str(len(target.split())))
			nb_en = nb_en + nb_src
			nb_trad = nb_trad + nb_tgt

	print("english: " + str(nb_en))
	print("trad: " + str(nb_trad))

elif FILE.endswith("crp"):
	i = 0 
	with open(FILE) as corpus:
		lines = corpus.readlines() 
		for k in range(0, len(lines)):
			if k == i :
				source = lines[k+1].strip("\n") 
				target = lines[k+2].strip("\n")
				
				nb_src = len(source.split()) 
				print(source + " " + str(len(source.split())))
				## count Chinese characters in string
				if flag == True:
					nb_tgt = len(target.replace(' ', ''))
					print(target + " " + str(nb_tgt))
				else:
					nb_tgt = len(target.split()) 
					print(target + " " + str(len(target.split())))

				nb_en = nb_en + nb_src
				nb_trad = nb_trad + nb_tgt

				i+=3 
	print("english: " + str(nb_en))
	print("trad: " + str(nb_trad))

