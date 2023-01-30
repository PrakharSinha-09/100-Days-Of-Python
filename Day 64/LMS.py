class library:
  count = 5
  bcount = 0
  books = [["HarryPotter", "Magic"], ["Cracking The Coding Interview", "Interview"],
           ["Python", "Language"], ["Java", "Language"], ["Flutter", "Technology"]]
  borrowed = list()
  personList = list()
  

  def addBooks(self):
    print("\n\t----Add a Book----\n")
    book = input("Enter the Book Name to add: ")
    type = input("Enter the Category of book: ")
    self.books.append([book, type])
    self.count += 1
    print("\n\t Sucessfuly Added")


  def showBooks(self):
    i = 1
    check = int(input("\nWhich Books do you want to see\n1-> Library Books\n2-> Borrowed Books\n\nEnter Here: "))

    if (check == 1):
      filter = input("\nEnter 'f' for filter OR Press Enter to continue: ").lower()

      if (filter == 'f'):
        checkC = input("\nType the Name of category: ")
        print(f"\nCategory {checkC}:\n")
        for book in self.books:
          if (checkC == book[1]):
            print(f"{book[0]}")

      else:
        print(f"\nLibrary Books:\t\tCategory:\n")
        for book in self.books:
          print(f"{i}. {book[0]}\t\t {book[1]}")
          i += 1

    elif (check == 2):
      print(f"\nBorrowed Books:\n")
      for bbook in self.borrowed:
        print(f"{bbook[0]}")


  def countBooks(self):
    print(f"\nTotal number of Library Books: {self.count}")
    print(f"\nTotal number of Borrowed Books: {self.bcount}")


  def borrowBooks(self):
    person = input("Enter your Name: ")
    self.personList.append(person)
    borrow = input("Enter a Book from Library you Want to borrow:\n")
    for book in self.books:
      b = 0
      if (borrow == book[0]):
        self.borrowed.append([borrow, book[1]])
        self.books.remove(book)
        self.count -= 1
        self.bcount += 1
        print(f"\n\t{borrow} Borrowed\n")

      else:
        b += 1

    if (b != 0):
      print("\nBook doesn't available at this time\n")


  def returnBooks(self):
    p = 0
    checkPerson = input("Enter your Name: ")
    for person in self.personList:
      if (checkPerson == person):
        for bbook in self.borrowed:
          self.books.append([bbook[0], bbook[1]])
          self.borrowed.remove(bbook)
          self.count += 1
          self.bcount -= 1
        print(f"\n\t Thanks for Returning! {bbook[0]}\n")
      else:
        p += 1
    if (p != 0):
      print("\nYou didn't Borrowed a book\n")


lib = library()

while True:
  choice = input("\nEnter 'a' for Add\nEnter 'b' for Borrow\nEnter 'c' for Count\nEnter 'r' for Return\nEnter 's' for show Books\n\nEnter here-> ").lower()
  if (choice == 'a'):
    lib.addBooks()
  elif (choice == 's'):
    lib.showBooks()
  elif (choice == 'r'):
    lib.returnBooks()
  elif (choice == 'b'):
    lib.borrowBooks()
  elif (choice == 'c'):
    lib.countBooks()

  play = input("\nWant to perform actions Type 'y' Otherwise 'n': ").lower()
  if (play == 'n'):
    break
  elif (play != 'y'):
    print("\nEnter in 'y' and 'n' only")
    break