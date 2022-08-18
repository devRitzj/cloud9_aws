"""
Your module description
"""
userReply = input("Do you need to ship a package? (Enter yes or no) :")
if userReply == "yes":
    print("We can help you ship that package!")
userReply = input("Would you like to buy \n 1 stamps \n 2. An Envelop \n 3. Make a Copy \n Enter 1, 2 or 3 for you choice : ")
if userReply == "1":
    print("We have many stamp designs to choose from.")
elif userReply == "2":
    print("We have many envelop sizes to choose from.")
elif userReply == "3":
    copies = input("How many copies would you like? Enter a number")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, Please come again")
    