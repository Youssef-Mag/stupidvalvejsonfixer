import json

#load the weird json
f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.split('"')
final = ""

i = 0
j = 0
try:
    for x in data:
       # print(x)
        ext = ""
        pre = ""
        x.replace("\n", "")
        #count up how many " we passed, if we pass 2 then put : if we pass 4 then put ,
        if "{" in x:
            i= 0
        if i == 1:
            ext = ":"
        if i ==3:
            #makes sure not to add comma at the end of a json
            if not "}" in data[j+1]:
                ext = ','
        
        #to add commas after }
        if "}" in x:
            if j+1 < len(data):
                if data[j+1].count("}") == 0:
                    pre = ","
        
        final += f'{x}{pre}"{ext}'

        i+=1
        j +=1
        if i >= 4:
            i = 0
except Exception as e:
    print(e)

#print(final[:len(final)-1])
f = open('out1.txt', 'w')
f.write(final[:len(final)-1])
f.close()
input("done")