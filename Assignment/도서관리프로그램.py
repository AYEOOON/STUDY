class Book():
    def __init__(self, title, author, publisher, isbn, loan):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.loan = False

    
    def BookInfo(self, file):
        file.write(self.title+",")
        file.write(self.author+",")
        file.write(self.publisher+",")
        file.write(self.isbn+",")

    def SaveBookInfo(self):
        try:
            with open(self.title.txt_file, "w") as file:
                self.BookInfo(file)
                print("책 정보가 저장되었습니다!")
        except:
          print("error")

