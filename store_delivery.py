a = []
b = []
c = []
x = []
y = []

def convertor(string1):
    a = string1.split(",")
    a[0] = (a[0].replace("[", ""))
    a[-1] = (a[-1].replace("]", ""))
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def checka():
    for i in a:
        if i in c:
            x.append(c.index(i))
    y = x.copy()
    y.sort()
    if x == y:
        x.clear()
        y.clear()
        return True
    else:
        x.clear()
        y.clear()
        return False
    
def checkb():
    for i in b:
        if i in c:
            x.append(c.index(i))
    y = x.copy()
    y.sort()
    if x == y:
        return True
    else:
        return False

my_file = open("inputfile.txt", "r")
out_file = open("output.txt", "a")
data = my_file.read()
new_lines = data.split("\n")
no_of_inputs = int(new_lines[0])
count = 1
while(count<=59):
    a = convertor(new_lines[count]).copy()
    b = convertor(new_lines[count+1]).copy()
    c = convertor(new_lines[count+2]).copy()

    if (checka() and checkb()):
        print("Valid")
        out_file.writelines("Valid")
        out_file.writelines("\n")
    else:
        print("Invalid")
        out_file.writelines("Invalid")
        out_file.writelines("\n")
    count = count+3

out_file.close()
my_file.close()