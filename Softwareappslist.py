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
        if (author == list[i].author):
            print(list[i].name, list[i].author, list[i].version, list[i].year, list[i].price)
            isPresent = 1
    if (isPresent == 0):
        print("Enter Valid Name")

def sortbyprice():
    n = len(list)
    for i in range(n - 1):
       for j in range(0, n - i - 1):
            if list[ j ].price > list[ j + 1 ].price:
                list[ j ], list[ j + 1 ] = list[ j + 1 ], list[ j ]

    for i in range(n):
        print(list[ i ].name, list[ i ].author, list[ i ].version, list[ i ].year, list[ i ].price)

def displaybyyear(year):
    isPresent = 0
    for i in range(len(list)):
        if (year == list[i].year):
            print(list[i].name, list[i].author, list[i].version, list[i].year, list[i].price)
            isPresent = 1
    if (isPresent == 0):
        print("Enter a Valid Year")

def sortbyauthoryear():
    n = len(list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ((list[ j ].author > list[ j + 1 ].author) or (list[ j ].author == list[ j + 1 ].author and list[ j ].year > list[ j + 1 ].year) ):
                list[ j ], list[ j + 1 ] = list[ j + 1 ], list[ j ]

    for i in range(n):
        print(list[ i ].name, list[ i ].author, list[ i ].version, list[ i ].year, list[ i ].price)

list = []
print("Enter Number of Inputs: ")
noofApps = int(input())
for i in range(noofApps):
    softwareName = input()
    authorName = input()
    version = input()
    year = int(input())
    price = int(input())
    list.append(Software(softwareName, authorName, version, year, price))
# list.append(Software('handwriter', 'pandi', 2.1, 2020, 20000))
# list.append(Software('passcheck', 'murugan', 3, 2019, 30000))
# list.append(Software('kadsfh', 'murugan', 3, 2020, 40000))
# list.append(Software('colorgame', 'sam', 1.1, 2018, 10000))
print("\n1.Display by author\n2.Sort by price\n3.Display details by given year\n4.Sort by author and publish year\n")
print("Enter Your Choice: ")
choice = int(input())
if (choice == 1):
    print("Enter Author Name")
    author = input()
    displaybyname(author)

elif (choice == 2):
    sortbyprice()

elif (choice == 3):
    print("Enter Year")
    year = int(input())
    displaybyyear(year)

elif (choice == 4):
    sortbyauthoryear()

else:
    print("Enter a Valid Choice")
