from typing import *

def dataTypes(type: str):
    match type:
        case ("Integer"):
            return("4")
        case ("Long"):
            return("8")
        case ("Float"):
            return("4") 
        case ("Double"):
            return("8") 
        case ("Character"):
            return("1")
        case _:
            return("Invalid Input")
            
dataTypes("Long")
