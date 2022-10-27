class Airport():
    
    def __init__(self,iata,name,location,city,country,website,phone):
        self.__iata = iata
        self.__name = name
        self.__location = location
        self.__city = city
        self.__country = country
        self.__website = website
        self.__phone = phone
        self.__operators = {}

    def getIata(self):
        return self.__iata
    def getName(self):
        return self.__name
    def getLocation(self):
        return self.__location
    def getCity(self):
        return self.__city
    def getCountry(self):
        return self.__country
    def getWebsite(self):
        return self.__website
    def getPhone(self):
        return self.__phone
    def getOperators(self):
        return self.__operators

    def addOperator(self,name,planes):
        self.__operators[name] = planes
    
    def deleteOperator(self,name):
        self.__operators.pop(name)
