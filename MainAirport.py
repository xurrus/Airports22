from controllerAirport import ControllerAirport

controller = ControllerAirport()

def getIata():
    iata = ""
    while True:
        iata = input("Enter the IATA: ")
        if len(iata) == 3:
            break
        print("¡Error entering the IATA! (AAA)")
        
    return iata.upper()


while True:
    print("")
    print("¡We have ",controller.countAirports()," airports!")
    print("1.- Import an airport")
    print("2.- Delete an airport")
    print("3.- Add a flight operator to an airport")
    print("4.- Delete a flight operator from an airport")
    print("5.- List airports by operators")
    print("6.- List number of planes by operator (all / by airport)")
    print("7.- Exit")
    option = int(input("Select an option: "))
    
    if option == 7:
        print("BYE")
        break
    #IMPORT AIRPORT
    elif option == 1:
        iata = getIata()
        if (controller.addAirport(iata)):
            print("Airport added!")
        else:
            print("Error adding the airport")

    #DELETE AIRPORT
    elif option == 2:
        iata = getIata()
        if (controller.deleteAirport(iata)):
            print("Airport deleted!")
        else:
            print("Error deleting")

    #ADD OPERATOR TO AN AIRPORT
    elif option == 3:
        iata = getIata()
        name = input("Enter the operator name: ")
        planes = int(input("Enter the planes of the operator: "))
        if controller.addOperator(iata,name,planes):
            print("Operator added!")
        else:
            print("Error adding operator")

    #DELETE OPERTAOR TO AN AIRPORT
    #Delete the operator from the airport
    elif option == 4:
        iata = getIata()
        name = input("Enter the operator name: ")
        if controller.deleteOperator(iata,name):
            print("Operator removed!")
        else:
            print("Error removing operator")

    #LIST AIRPORTS BY OPERATORS
    #List all the airports where the operator works
    elif option == 5:
        name = input("Enter the operator name: ")
        aeropuertos = controller.list5(name)
        if len(aeropuertos) > 0:
            print("The operator ",name," works in this airports:")
            for a in aeropuertos:
                print("\n",a.getName(),a.getLocation(),a.getIata())
        else:
            print("Error. This operator doesn't works in any airport")

    #LIST NUMBER OF PLANES BY OPERATORS
    elif option == 6:
        print("\n1)Count planes in all airports")
        print("\n2)Count planes in one airport")
        coption = int(input("Select count option: "))
        if coption == 1:
            operator = input("Enter the operator name: ")
            planes = controller.list6General(operator)
            if planes > 0:
                print("The operator ",operator," has ",planes," planes in all airports")
            else:
                print("Error. This operator doesn't have any plane in any airport")

        elif coption == 2:
            operator = input("Enter the operator name: ")
            iata = getIata()
            planes = controller.list6Airport(iata,operator)
            if planes > 0:
                print("The operator ",operator," has ",planes," planes in ",iata," airport")
            else:
                print("Error. This operator doesn't have any plane in ",iata," airport")


