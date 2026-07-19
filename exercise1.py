#START
ratings = 0
low = 0
medium = 0
high = 0
while True:
    rating = int(input("rating? "))
    if rating == -1:
        break
    if rating > 5 or rating < 0:
        print("rating is invalid")
        continue
    if rating == 1 or rating ==2:
        low+=1
    elif rating ==3:
        medium+=1
    elif rating ==4 or rating ==5:
        high+=1
    ratings+=1
print("valid ratings: " + str(ratings))
print("low (1-2): " + str(low))
print("medium (3): " + str(medium))
print("high (4-5): " + str(high))

#STOP