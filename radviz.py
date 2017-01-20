
infilename = "browncorpus_stemtowords_2.txt"
Stems = dict()
stemcount = dict()
with open (infilename, "rt" ) as infile:
	for line in infile:
                if len(line) == 0 or line[:3]=="---":
                     continue
                items = line.split()
                stem = items[0]
                Stems[stem] = dict()
                stemcount[stem]= items[1]
                items=items[3:]
                number_of_items = int(len(items)/3)
                for wordno in range(number_of_items):
                        word = items[wordno*3 ]
                        wordcount =items[wordno*3 + 1]
                        Stems[stem][word]=wordcount     
                print (stem, stemcount[stem], Stems[stem])
