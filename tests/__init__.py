import time
from frontend import frontend
from backend import backend

def test_frontend():
    # TODO: Run all frontend tests
    frontend( 42 )

def test_backend():
    # TODO: Run all backend tests
    backend( 80 )

def test_all():
    print("Testing frontend ")
    test_frontend()
    # sleep for 1 second
    time.sleep(1)
    # continue with the rest 
    print("Testing backend ")
    test_backend()
