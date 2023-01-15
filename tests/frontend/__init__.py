"""
    Frontend main test script
    This is meant as an example
    to illustrate how this file can be used in other tests
"""

def m5( x ):
    return x - 5 

def a5( x ):
    return x + 5

def test1():  # frontend test 1
    assert( m5(40) ) == 35

def test2(): # frontend test 2
    assert( a5(55) ) == 60

if __name__ == "__main__":
   
    print("Running frontend test1: ")
    test1()

    time.sleep(1)

    print("Running frontend test2: ")
    test2()
