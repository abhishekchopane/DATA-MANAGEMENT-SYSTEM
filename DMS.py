#   MINI PROJECT PROGRAM TO ENTER AND MODIFY SALARY ENTRIES

def sal(n):
    a = []
    b = []
    if n == 1:
        x = int(input("Enter No of People\n"))
        for y in range(2*x):
            c = input("Enter Field\n")
            a.append(c)
        print("Your Data has been Successfully Entered\n", a)
        k = open('Salary Details.txt', 'w')
        for g in range(2*x):
            k.write("%d " % (g+1))
            k.write("%s\n" % a[g])
        print("File Saved Successfully")
        k.close()
    elif n == 2:
        k = open('Salary Details.txt', 'r')
        print(k.read())
    elif n == 3:
        k = open('Salary Details.txt', 'r')
        b = k.readlines()
        print(b)
        k.close()
        x = int(input("Enter Entry Number to Edit\n"))
        o = input("Enter Field")
        b[x-1] = "%d %s\n" % (x, o)
        k = open('Salary Details.txt', 'w')
        k.writelines(b)
        print("Your Data has been Successfully Replaced\n")
        print("File Saved Successfully")
        k = open('Salary Details.txt', 'r')
        print(k.read())
        k.close()
    elif n == 4:
        k = open('Salary Details.txt', 'r')
        b = k.readlines()
        print(b)
        k.close()
        x = int(input("Enter Field Number to Clear\n"))
        if x % 2 == 0:
            e = b.pop(x - 1)
            e = b.pop(x - 2)
        else:
            e = b.pop(x - 1)
            e = b.pop(x - 1)
        k = open('Salary Details.txt', 'w')
        k.writelines(b)
        print("Your Data has been Successfully Removed\n")
        k = open('Salary Details.txt', 'r')
        print(k.read())
        k.close()


print("1. Add New Entries\n2. View Existing Entries\n3. Modify Existing Entries\n4. Delete Existing Entries\n")
n = int(input("Enter The Operation you Wish to Execute\n"))
sal(n)
