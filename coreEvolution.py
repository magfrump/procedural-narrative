from graphics import *
from random import *
from math import *
#wind = GraphWin('Face', 640, 480)


def Draw(win,size,color,scales,fur,claws,spacing=0):
    body = Circle(Point(2*size,2*size),size)
    body.setFill(color_rgb(color,0,0))
    body.draw(win)

    for _ in range(0,scales):
        randlength = random()
        randangle = random()*2
        randx,randy = 2*size-size*randlength*cos(randangle),2*size-size*randlength*sin(randangle)
        scale = Polygon([Point(randx,randy),Point(randx+4,randy+4),Point(randx+9,randy)])
        scale.setFill("green")
        scale.draw(win)

    for _ in range(0,fur):
        randlength = random()
        randangle = random()*2
        randx,randy = 2*size-size*randlength*cos(randangle),2*size-size*randlength*sin(randangle)
        fur = Line(Point(randx,randy),Point(randx-10,randy-10))
        fur.setFill("brown")
        fur.draw(win)
    
    for _ in range(0,claws):
        randlength = random()/2+.5
        randangle = random()-.5
        randx,randy = 2*size+size*randlength*cos(randangle),2*size+size*randlength*sin(randangle)
        scale = Polygon([Point(randx,randy),Point(randx+10,randy+5),Point(randx+4,randy-1)])
        scale.setFill("red")
        scale.draw(win)

        
class Animal:
    """Not a simple class."""

    def __init__(self,Traits):
        #Inherit Genotypic traits
        self.size=Traits[0]
        self.carnivory=Traits[1]
        self.herbivory=Traits[2]
        self.fur=Traits[3]
        self.scales=Traits[4]
        self.blubber=Traits[5]
        self.r=Traits[6]
        self.K=Traits[7]
        self.webbing=Traits[8]
        self.claws=Traits[9]
        self.color=Traits[10]
        self.grip=Traits[11]
        self.sleep=Traits[12]
        self.speed=Traits[13]
        self.environment=None

        #calculate some phenotypic traits
        self.Power = (self.size+self.blubber+self.scales)*(self.size + self.claws)
        self.EnergyCap = (3*(self.r*(self.size**2)+self.blubber)+2*(self.r+self.scales+self.carnivory) + (self.K+self.webbing+self.claws+self.grip+self.herbivory))
        self.energy = 0
        self.fat = self.size+self.blubber-self.scales

    def Movement(self,environment):
        move = self.size + 2*self.speed - self.blubber
        move += self.webbing*(environment.moisture - environment.TreeSize)
        move += self.grip*environment.TreeSize
        self.environment = environment.name
        return move

    def Display(self,num,draw=True,wind=None):
        print("Creature number ",num," has the following traits:")
        print("Carn: ",self.carnivory,"Herb: ",self.herbivory)
        print("r,K: ",self.r,self.K)
        print("energy: ",self.energy,"/",self.EnergyCap)
        if draw:
            if wind==None:
                wind = GraphWin('Creature'+str(num), 640, 480)
            Draw(wind,self.size*10+20,self.color,self.scales,self.fur,self.claws)

    @classmethod
    def offspring(cls,animal):
        Traits = []
        Traits.append(max(1,animal.size-2+ randint(0,4)))
        Traits.append(min(max(0,animal.carnivory-2+ randint(0,4)),10))
        Traits.append(min(max(0,animal.herbivory-2+ randint(0,4)),10))
        Traits.append(max(0,animal.fur-2+ randint(0,4)))
        Traits.append(max(0,animal.scales-2+ randint(0,4)))
        Traits.append(max(0,animal.blubber-2+ randint(0,4)))
        Traits.append(max(1,animal.r-2+ randint(0,3)))
        Traits.append(max(0,animal.K-2+ randint(0,4)))
        Traits.append(max(0,animal.webbing-2+ randint(0,4)))
        Traits.append(max(0,animal.claws-2+ randint(0,4)))
        Traits.append(max(0,animal.color-4+ randint(0,8)))
        Traits.append(max(0,animal.grip-2+ randint(0,4)))
        Traits.append(min(max(0,animal.sleep-2+ randint(0,4)),24))
        Traits.append(max(0,animal.speed-2+ randint(0,4)))
        return cls(Traits)

class Environment:

    def __init__(self,Traits):
        self.WinterTemp=Traits[0]
        self.SummerTemp=Traits[1]
        self.moisture=Traits[2]
        self.color=Traits[3]
        self.plantLife=Traits[4]
        self.TreeSize=Traits[5]
        self.name = Traits[6]
        self.AnimalLife = 0


def Predation(prey,predator,environment):
    #describes an encounter between two animals in an environment
    #returns None if they do not interact
    #otherwise returns 0 for animal1 eats animal2
    if (predator.Power > prey.Power):
        if  randint(0,23) < predator.sleep:
            #predator is sleeping
            return None
        if  randint(0,254)< prey.color-environment.color:
            #prey successfully camouflaged
            return None
        if prey.Movement(environment) > predator.Movement(environment):
            #prey runs away
            prey.energy-=predator.Movement(environment)
            return None
        predator.energy+=prey.fat
        prey.energy-=2*prey.fat
        environment.AnimalLife+=1
        return 0

def Forage(animal,environment):
    #adjusts the animal's energy based on its environment
    #returns 1 if the animal decides to move

    if  randint(0,10) <environment.plantLife:
        animal.energy += 3*sqrt(4*animal.herbivory)
        environment.plantLife -= sqrt(animal.herbivory)

    if  randint(0,10)<environment.AnimalLife:
        animal.energy+=2*sqrt(animal.carnivory*4)
        environment.AnimalLife -= sqrt(animal.carnivory)

    season =  randint(0,3)
    if season == 0:
        weather = (environment.WinterTemp)/(animal.fur+animal.blubber+1)
    if season == 2:
        weather = environment.SummerTemp*animal.blubber/(1+animal.scales)
    else:
        weather = min(animal.fur,animal.scales)
    
    animal.energy -= weather/(1+animal.sleep)

    if  randint(0,100) < 5 and weather>animal.energy/2:
        #print("Migration occurs!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return 1
    else:
        return None
    
#Environments are forest, dessert, mountain        
EnvironmentList = [Environment([1,0,10,0,100,10,"Forest"]),Environment([2,4,1,250,10,0,"Dessert"]),Environment([4,1,3,125,50,2,"Mountain"])]
#EnvironmentList = [Environment([10,5,10,0,100,10,"Forest"])]
#start with a generic amoeba in every environment
AnimalList = [[Animal([1,1,3,0,0,0,2,0,0,0,0,0,0,0]) for num in range(0,100)] for _ in EnvironmentList]

num_gens = 10000

for x in range(0,num_gens):
    for envir in range(0,len(EnvironmentList)):
        environ=EnvironmentList[envir]
        environ.plantLife+=(environ.moisture*400)+environ.plantLife
        newAnimalList=[]
        for anim in AnimalList[envir]:
            if Forage(anim,environ)==1:
                newenv= randint(0, len(AnimalList)-1)
                AnimalList[newenv].append(anim)
            for a in range(0,int(sqrt(anim.carnivory))):
                Predation(AnimalList[envir][ randint(0,len(AnimalList[envir])-1)],anim,environ)
            if anim.energy >= anim.EnergyCap:
                for y in range(0,anim.r):
                    newAnimalList.append(Animal.offspring(anim))
                anim.energy -= anim.EnergyCap
                #print("BABBY FORMD")
            if anim.energy>= anim.EnergyCap/5 and anim.EnergyCap>0:
                newAnimalList.append(anim)
            else:
                environ.AnimalLife+=anim.fat
        if len(newAnimalList) < .9*len(AnimalList[envir]):
            print("DECLINE!")
        if len(newAnimalList) > 2*len(AnimalList[envir]):
            print("EXPLOSION!")
        if (x%30==0):
            print("Population: ",len(newAnimalList)," in generation ",x)
        if len(newAnimalList)>=1:
            shuffle(newAnimalList)
            AnimalList[envir]=newAnimalList[:100]
        else:
            print("EXTINCTION! In generation ",x)
            break

for x in AnimalList:
    carn=0
    herb=0
    omn=0
    mamm=0
    rept=0
    other=0
    for y in x:
        if y.carnivory>3*y.herbivory:
            carn+=1
        elif y.herbivory > 3*y.carnivory:
            herb+=1
        else:
            omn+=1
        if y.fur > 3*y.scales:
            mamm+=1
        elif y.scales > 3*y.fur:
            rept+=1
        else:
            other+=1
        if  randint(0,len(x))<5:
            y.Display(x.index(y))
            print("\n")
    print("In this environment, the ecology has:")
    print(carn," carnivores, ",herb," herbivores, and ",omn," omnivores")
    print(mamm," mammals, ",rept," reptiles, and ",other," other creatures")
