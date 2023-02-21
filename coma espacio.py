import glob
text_file = glob.glob('*.txt')


for filename in glob.glob('*.txt'):
    with open(filename, 'r') as fo:
        for ln in fo:
            if ln.startswith("	MALICIOUS: "):
                mal=(str(ln[12:]).replace(', ','\n'))
            if ln.startswith("	SUSPICIOUS: "):
                sus=(str(ln[13:]).replace(', ','\n'))
            if ln.startswith("	INFO: "):
                inf=(str(ln[7:]).replace(', ','\n'))    
        with open (str("Actividades") + '.txt','w') as opf:
            opf.write("MALICIOUS: \n" + mal + "\n")
            opf.write("SUSPICIOUS: \n" + sus + "\n")
            opf.write("Info: \n" + inf + "\n")



