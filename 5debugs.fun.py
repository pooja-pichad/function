# Question 5

# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.
# (number of bugs)
 
# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)
#         else:
#             Print(far)
#     distance(20,30)


def distance(kms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print("median")
    else:
        print("far")
distance(20)