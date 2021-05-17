def split():
    sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
    i=0
    new=[]
    while i<len(sentence):
        a=sentence.split()
        new.append(a)
    i+=1
    print(new)
split()