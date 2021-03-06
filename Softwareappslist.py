class Software:
    def __init__(self, name, author, version, year, price):
        self.name = name
        self.author = author
        self.version = version
        self.year = year
        self.price = price

def displaybyname(author):
    isPresent = 0
    for i in range(len(list)):
        if (author == list[i].author):                                                                             #validating author name
            print(list[i].name, list[i].author, list[i].version, list[i].year, list[i].price)
            isPresent = 1
    if (isPresent == 0):
        print("Enter Valid Name")

def sortbyprice():
    n = len(list)
    for i in range(n - 1):                                                                                          #sorting using bubble sort
       for j in range(0, n - i - 1):
            if list[ j ].price > list[ j + 1 ].price:
                list[ j ], list[ j + 1 ] = list[ j + 1 ], list[ j ]

    for i in range(n):
        print(list[ i ].name, list[ i ].author, list[ i ].version, list[ i ].year, list[ i ].price)

def displaybyyear(year):
    isPresent = 0
    for i in range(len(list)):
        if (year == list[i].year):                                                                                  #validating year
            print(list[i].name, list[i].author, list[i].version, list[i].year, list[i].price)
            isPresent = 1
    if (isPresent == 0):
        print("Enter a Valid Year")

def sortbyauthoryear():
    n = len(list)
    for i in range(n - 1):                                                                                           #bubble sort
        for j in range(0, n - i - 1):
            if ((list[ j ].author > list[ j + 1 ].author) or (list[ j ].author == list[ j + 1 ].author and list[ j ].year > list[ j + 1 ].year) ):
                list[ j ], list[ j + 1 ] = list[ j + 1 ], list[ j ]

    for i in range(n):
        print(list[ i ].name, list[ i ].author, list[ i ].version, list[ i ].year, list[ i ].price)

list = []
noofApps = int(input("Enter Number of Inputs: "))
for i in range(noofApps):
    print("Enter Software Name, Author Name, Version, Year, Price: ")                                              #getting user input
    softwareName = input()
    authorName = input()
    version = input()
    year = int(input())
    price = int(input())
    list.append(Software(softwareName, authorName, version, year, price))

print("\n1.Display by author\n2.Sort by price\n3.Display details by given year\n4.Sort by author and publish year\n")
condition = True
while (condition):
    choice = int(input("Enter Your Choice: "))
    if (choice == 1):
        author = input("Enter Author Name")
        displaybyname(author)           

    elif (choice == 2):
        sortbyprice()

    elif (choice == 3):
        year = int(input("Enter Year"))
        displaybyyear(year)

    elif (choice == 4):
        sortbyauthoryear()

    else:
        print("Enter a Valid Choice")

    print("Do you want to continue(0/1): ")
    yorn = int(input())
    if(yorn == 0):
        condition = True
    else:
        condition = False




