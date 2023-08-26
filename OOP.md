# Python OOP

Classes are widely used in OOP-oriented languages to create user-defined data structures.

Let's define a class:
```
class Dog:
    pass
```
There are a number of properties to be added to this Dog class, including name, age, coat color, and breed.

For instance:
```
class Dog:
    species = 'Scotch Terrier'
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Instantiate a class:

```
myDog = Dog("Lerik", 5)
myDog.name
myDog.age
myDog.species
```

Let's add method to print out more detailed description (int case myDog gets lost 😉 )

```
class Dog:
    species = 'Scotch Terrier'
    def description(self):
        return f"{self.name} is {self.age} years old"
    def bark(self, sound):
        return f"{self.name} says {sound}"
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

And use declared methods:

```
myDog = Dog('Miles', 6)
myDog.description()
myDog.bark("Woof Woof")
``` 

Instances of a class are called objects:

```
print(myDog)
```

Another example of a car class:

```
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
# creating two instances:
yellow_car = Car(color="yellow", mileage=19800)
green_car = Car(color="green", mileage=35000)
```

Print out fields of a car object:

```
for car in (yellow_car, green_car):
    print(f"The {car.color} car has {car.mileage} miles")
```

To create a child (inherited class):
```
class Buggy(Car):
    transmission = 4
    def Transmission(self)
        return self.transmission*self.milage
class Rover(Car):
    transmission = 2
    def Transmission(self)
        return self.transmission*self.milage

newBuggyInGarage = Buggy("red", 100)
newRoverInGarage = Rover("pink", 80)
```
