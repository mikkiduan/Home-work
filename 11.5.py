this = ["I", "am", "not", "a", "crook"]

that = ["I", "am", "not", "a", "crook"]

print("Test 1: {0}".format(this is that))

that = this

print("Test 2: {0}".format(this is that))



""
import sys

def test(did_pass):

    linenum = sys._getframe(1).f_lineno

    if did_pass:

        msg = "Test at line {0} ok.".format(linenum)

    else:

        msg = ("Test at line {0} FAILED.".format(linenum))

    print(msg)







def add_vectors(u,v):

    mylist=[]

    for i in range(len(u)):

        mylist.append(u[i]+v[i])

    return mylist



def test_suite():

    test(add_vectors([1, 1], [1, 1]) == [2, 2])

    test(add_vectors([1, 2], [1, 4]) == [2, 6])

    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])




test_suite()

""