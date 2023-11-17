def capitalize(string):
  string=string.lower()
  return string[0].upper() + string[1:]

def addCity(cities):
  city=input("please enter city name: ")
  city=capitalize(city)
  if city in cities:
    print("city exists")
  else:
    cities.append(city)
  return cities

def addDriver(drivers,driversName, cities):
  newDriver={}
  print("available drivers are: ", driversName)
  driver=input("chose driver: ")
  driver=capitalize(driver)
  if driver in driversName:
    print("available cities are ", cities)
    cities_input=input("please enter cities name in order of route(seperated by space): ")
    route=cities_input.split()
    if(not set(route).issubset(set(cities))):
      print("some cities are not availabe")
    else:
      newDriver["name"]=driver
      newDriver["route"]=route
      drivers.append(newDriver)
    print(drivers)
  else:
    print('driver name not found')
  return drivers
       
def addCityToRoute(drivers_name, cities, drivers):
  print("available drivers are: ", drivers_name)
  driverName=input("chose driver: ")
  driverName=capitalize(driverName)
  if (not driverName in drivers_name):
     print("Driver doesnt exist")
  else:
    print("available cities are: ", cities)
    cityName=input("chose city ")
    cityName=capitalize(cityName)
    if (not cityName in cities):
      print("City doesnt exist")
    else:
      for driver in drivers:
        if (driverName == driver["name"] and (not cityName in driver["route"])):
          print("0. To add to the beginning of the route\n-1. To add to the end of the route\n#. (any other number) to add that city to the given index\n")
          index=int(input("chose option"))
          if index==0:
            driver["route"].insert(0,cityName)
          elif index==-1:
            driver["route"].append(cityName)
          else:
            print("The driver is new with no previous route, add Driver")
            addDriver(drivers,driverName, cities)
        else:
          print("driver not found")
    print(drivers)
    return drivers

def removeCity(drivers):
  driversName=[]
  for driver in drivers:
    driversName.append(driver["name"])
  print("available working drivers names: ", driversName)
  driverName=input("chose driver: ")
  driverName=capitalize(driverName)
  if driverName in driversName:
    for selectedDriver in drivers:
      if driverName == selectedDriver["name"]:
        print("available cities for this driver: ", selectedDriver["route"])
        cityName=input("chose city to remove: ")
        cityName=capitalize(cityName)
        if cityName in selectedDriver["route"]:
          driver["route"].remove(cityName)
        else:
          print("city not found")
  else:
    print("driver not found")
  return drivers

def deliverbityOfPackage(drivers,cities):
  availableDriver=[]
  cityName=input("chose destination: ")
  cityName=capitalize(cityName)
  if cityName in cities:
    for driver in drivers:
      if cityName in driver["route"]:
        availableDriver.append(driver["name"])
    print("available drivers are", availableDriver)
  else:
    print("city not found")

  
def openMenu():
  cities=["Beirut","Tripoly","Bekaa","Jounieh","Tyre"]
  drivers_name=["Ali","Pascal","Ramy"]
  drivers=[]
  choice=100

  while choice !=5:
    print("Enter")
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from a driver’s route")
    print("5. To check the deliverability of a package")

    choice=int(input())

    if choice==1:
      cities=addCity(cities)
    elif choice ==2:
      drivers=addDriver(drivers,drivers_name,cities)
    elif choice ==3:
      drivers=addCityToRoute(drivers_name,cities,drivers)
    elif choice ==4:
      drivers=removeCity(drivers)
    elif choice ==5:
      deliverbityOfPackage(drivers,cities)
    else:
      print("ivalid input")
  
def mainMenu():
  choice=100
  while choice !=2:
    print("Enter")
    print("1. to open menu")
    print("2. to close the program")
    
    choice=int(input())
    
    if choice==1:
      print("opening menu...")
      openMenu()
    elif choice ==2:
      print("good bye")
    else:
      print("ivalid input")


mainMenu()