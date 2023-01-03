nominee1= input("Enter the name of 1st nominee :")
nominee2= input("Enter the name of 2nd nominee :")

nom1_votes=0
nom2_votes=0

voter_id=5

no_of_voter = 5
print("Press 1 to vote for",nominee1)
print("Press 2 to vote for",nominee2)

        
while True:
    if voter_id == 0:
        print("Voting session terminated")

        if nom1_votes > nom2_votes:
            percent = (nom1_votes / no_of_voter) * 100
            print(nominee1 ,"has won the election with", percent ,"% votes" )
            
        elif nom2_votes > nom1_votes:
            percent = (nom1_votes / no_of_voter) * 100
            print(nominee2 ,"has won the election with", percent ,"% votes" )
        
        elif nom1_votes == nom2_votes :
            print("Both have equal votes")
            
        else:
            voter = int(input("Enter your input id"))
            
        if voter in voter_id:
            print("You are a voter")
        
  
    vote = int(input("Enter your vote"))
        
    if vote == 1:
        nom1_votes += 1
        voter_id = voter_id-1
        print( "Thank you for voting ")
    
            
    elif vote == 2:
        nom2_votes += 1
        voter_id = voter_id-1
        print("Thank you for voting ")
    
        
    elif vote>2:
        print("Invalid option")
    
    
    else:
        print("You have already voted")

        
        
    vote = int(input("Enter your vote"))
        
    if vote == 1:
        nom1_votes += 1
        print( "Thank you for voting ")
        
            
    elif vote == 2:
        nom2_votes += 1
        print("Thank you for voting ")
        
        
    elif vote>2:
        print("Invalid option")
        
    
    else:
        print("You have already voted")
        