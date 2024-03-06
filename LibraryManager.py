books_list=[]
authors_set=set()
books_dict={}
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"]="John Smith"

books_list.append("Data Structures and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data Sturctures and Algorithms"]="Jane Doe"

books_list.append("machine Learning Basis")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basis"]="Alice Jonhson"

search_title=input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author:{books_dict[searh_title]}")
else:
    print("Book not found!")

print("List of Books:")
for book in books_list:
    print("book")

remove_title=input("Enter the title of the book to remove or else enter to skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("book remoe successfully!")
    print("Books available:",books_list)
    
else:
    print("Book not found")




