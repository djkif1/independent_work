from locust import User, task
from calc import calculate_some_data
class MyFirstTest():


    def on_start(self)-> None:
        print("We start our test")

    def first(self):
        calculate_some_data()
        print("first test")
        pass

    def second(self):
        calculate_some_data()
        print("first test")
        pass

    def on_stop(self)-> None:
        print("We finished our test")