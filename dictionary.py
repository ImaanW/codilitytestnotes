
#RETURN VALUE FROM DICT
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#CHANGE VALUE
car["year"]= 2020

#ADD VALUE
car["color"] = "red"
# REMOVE MODEL
car.pop("model")
#CLEAR
car.clear()
