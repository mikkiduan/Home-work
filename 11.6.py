import sys

def test(did_pass):

    linenum = sys._getframe(1).f_lineno

    if did_pass:

        msg = "Test at line {0} ok.".format(linenum)

    else:

        msg = ("Test at line {0} FAILED.".format(linenum))

    print(msg)



def dot_product(u,v):

    mylist=[]

    for i in range(len(u)):

        mylist.append(u[i]*v[i])

    return mylist





def test_suite():

    test(dot_product([1, 1], [1, 1]) == 2)

    test(dot_product([1, 2], [1, 4]) == 9)

    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)



test_suite()