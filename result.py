import pickle              # import module first

f = open('winner.pkl', 'rb')   # 'r' for reading; can be omitted
mydict = pickle.load(f)         # load file content as mydict
f.close()

print(mydict)
# prints {'Lisa': 98, 'Bart': 75, 'Milhouse': 80, 'Nelson': 65}