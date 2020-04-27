import json
import view_corona
import model_corona
global provi
    


def GetChoice():
    choice = input(view_corona.StartProcess())
    if choice =='q' or choice == "Q":
        view_corona.EndProcess()
    elif choice=='N' or choice =='n' :
        country = input(view_corona.CountryName())
        GetCoronaDetail(country)
    else:
        view_corona.InvalidEntry()

def GetCoronaDetail(country):
    model_corona.CoronaDetail(country)
    with open('D:\Paritosh_Corona\corona.txt') as file:
        data = json.load(file)
    if data["data"]["covid19Stats"][0]["province"] == '':
        view_corona.ViewCoronaDetail(data,0)
    #print("confirmed death is {}".format(data["data"]["covid19Stats"][0]["confirmed"]))
    #print("On {} Death is {}".format(data["data"]["covid19Stats"][0]["lastUpdate"],data["data"]["covid19Stats"][0]["deaths"]))
    else:
        province_name = input(view_corona.EnterProvince())
        i=0
        length_val = len(data["data"]["covid19Stats"])
        while(i<length_val):
            if data["data"]["covid19Stats"][i]['province'] == province_name:
                provi = province_name
                i=i+1
                break
            else:
                provi="None"
                i=i+1
            
        k=0
        if(provi!="None"):
            while(k<length_val):
                if data["data"]["covid19Stats"][k]["province"] == provi:
                    view_corona.ViewCoronaDetail(data,k)
                    #print("confirmed death is {}".format(data["data"]["covid19Stats"][k]["confirmed"]))
                    #print("On {} Death is {}".format(data["data"]["covid19Stats"][k]["lastUpdate"],data["data"]["covid19Stats"][k]["deaths"]))
                    k=k+1
                    break
                else:
                    k=k+1
        else:
            print(view_corona.InvalidEntry())


GetChoice()
