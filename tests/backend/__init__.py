import time
def backend(x):
    return x / 5

def test_db_connection():
    print("Testing database connection: ")
    return True

def test1():
    assert( backend(40) ) == 8.0

if __name__ == "__main__":
    
    assert(test_db_connection() == True)
    
    time.sleep(1)
    
    print("Running test1: ")
    test1()
