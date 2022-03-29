f = open('poems.txt')
t = f.read()
if 'twinke' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()        