from curses import keyname
from airport import Airport
import AirportAPI as api

class ControllerAirport():
    def __init__(self):
        self.__airports = {}
    
    '''
    #1 IMPORT AIRPORT
    def addAirport(self,iata,name,location,city,country,website,phone):
        if iata in self.__airports:
            return False
        newAirport = Airport(iata,name,location,city,country,website,phone)
        self.__airports[iata] = newAirport
        return True
    '''
    #COUNT THE AIRPORTS
    def countAirports(self):
        return len(self.__airports)

    #1 CREATES AN AIRPORT FROM THE IATA AND ADDS IT TO OUR LIST
    def addAirport(self,iata):
        if iata in self.__airports:
            return False
        newAirport = api.getAirport(iata)
        self.__airports[iata] = newAirport
        return True

    #2 DELETES AN AIRPORT SEARCHING THE IATA, IF THIS PLANES ARE 0
    def deleteAirport(self,iata):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        operators = airport.getOperators()
        if len(operators) > 0:
            return False
        self.__airports.pop(iata)
        return True
            
    #3 ADD OPERATOR
    def addOperator(self,iata,name,planes):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.addOperator(name,planes)
        return True

    #4 REMOVE OPERATOR FROM AIRPORT
    def deleteOperator(self,iata,name):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.deleteOperator(name)
        return True

    #5 LIST ALL THE AIRPORTS WHERE THE OPERATOR WORKS
    def list5(self,ope):
        aeropuertos = []
        for key,value in self.__airports.items():
            if ope in value.getOperators():
                aeropuertos.append(value)
        return aeropuertos

    def list6General(self,operator):
        count = 0
        for key,value in self.__airports.items():
            if operator in value.getOperators():
                planes = value.getOperators()[operator]
                count += planes
        return count

    def list6Airport(self,iata,operator):
        count = 0
        if iata in self.__airports:
            aeropuerto = self.__airports[iata]
            if operator in aeropuerto.getOperators():
                operadores = aeropuerto.getOperators()[operator]
                count += operadores
        return count

        