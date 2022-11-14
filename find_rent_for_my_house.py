
def returnResult() -> int:
    upfront_cost=50000000
    starting_rent=90000
    counter=0
    while(upfront_cost>0):
        upfront_cost=upfront_cost-starting_rent
        counter=counter+1
        if (counter%12==0):
            starting_rent=starting_rent+(starting_rent*0.1)
    print(counter)

#returnResult()

