print("You ready Bitches?!!!\n Rock.....\nPaper.....\nScissors.....")

Roc = "Rock"
Pap = "Paper"
Sci = "Scissors"
p2 = ""
p1 = ""
while p2 != "Man that's enough game for today !":
	p1 = input("What do choose to do? Choose Wisely my friend! \n")
	print("Player2 won't be able to see what you have chosen\n" * 50)
	p2 = input("What do you choose to do ?\n Rock ?\n..... Paper ?\n..... Scissors?.....\n")
	if p1 == "You cheated !":
		break
#The shortest method really felt right

	if (p1 == Roc and p2 == Sci) or (p1 == Sci and p2 == Pap) or (p1 == Roc and p2 == Pap): 
		# USING THE OR OPERATOR I CLUBBED ALL THE CONDITIONS TOGETHER !!! SO IF ANY ONE OF THEM WOULD BE TRUE , PLAYER1 WILL WIN
		print("player1 has won the game ! Congratulations")
	elif (p1 == Sci and p2 == Roc) or ( p1 == Pap and p2 == Sci) or (p1 == Pap	and p2 == Roc):
		# USING THE OR OPERATOR AS I DID FOR PLAYER1 . NOW THE SAME CAN BE DONE FOR PLAYER2
		print("Player2 has won ! Congratulations")
	elif (p1 == Pap and p2 == Pap) or (p1 == Roc and p2 == Roc) or (p1 == Sci and p2 == Sci):
		print("It is draw !")
	else:
		print("Okay")



#Another Way to Make this game is as follows:
# We CAn use Nested conditionals :
#if p1 == "Roc":
   #if p2 == "Sci"


# THIS IS THE LONG METHOD AND ALSO I HAVE TO CHECK WHERE I WENT WRONG BECAUSE IT WASN'T DOING THINGS CORRECTLY
	#elif p1 == Sci and p2 == Pap:
	#print("Player1 has won ! Congratulations")
#elif p1 == Pap and p2 == Sci:
#	print("Player2 has won ! Congratulations")
#elif p1 == Roc and p2 == Pap:
#	print("Player1 has won ! Congratulations")
#elif p1 == Pap	and p2 == Roc:
#	print("Player2 has won ! Congratulations")
