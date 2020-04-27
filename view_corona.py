def StartProcess():
    print("Check for Corona Data: ")
    print("[N] for new Searh: ")
    print("[Q] for quit")
    return "Enter Your Choice: "

def CountryName():
    return "Enter Country Name: "


def EndProcess():
    print("Thanks For using Corona Database")
    return

def InvalidEntry():
    return "This is Invalid Entry"

def Country():
    return "Enter Country Name"

def GetCOuntryDetail():
    return "This is country Detail"

def EnterProvince():
    return "Enter Province Name:"

def ViewCoronaDetail(data,index):
    print("Last updated date for Death is  :\t",data["data"]["covid19Stats"][index]["lastUpdate"])
    print("Confirmed Death is  :\t",data["data"]["covid19Stats"][index]["confirmed"])
    print("Total death today is  :\t",data["data"]["covid19Stats"][index]["deaths"])

    
