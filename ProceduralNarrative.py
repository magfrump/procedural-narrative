#Booker story structures
Monster = {"anticipation":{},"dream":{},"frustration":{},"nightmare":{},"resolution":{}}

#Polti/Gozzi dramatic situations
Supplication = {"characters":["Persecutor","Supplicant","Authority"], "text":"Persecutor accuses Supplicant of wrongdoing, and Authority makes a judgment against Supplicant."}
Deliverance = {"characters":["Unfortunate","Threatener","Rescuer"],"text":"Unfortunate has caused a conflict, and Threatener is trying to carry out justice, but Rescuer saves Unfortunate."}
CrimePursued = {"characters":["Criminal","Avenger"],"objects":["Thing"],"text":"Criminal steals Thing, and Avenger pursues to bring Criminal to justice."}
KinVengeance = {"characters":["Guilty","Avenging","Relative"],"text":"Guilty, Avenging, and Relative are all related, but Guilty did something wrong and Avenging is pissed!"}
Pursuit = {"characters":["Fugitive"],"objects":["Punishment"],"text":"Fugitive flees evil Punishment for a misunderstood conflict."}
Disaster = {"characters":["Power","Enemy"],"text":"Power falls from their place after being defeated by Enemy."}
Cruelty = {"characters":["Unfortunate","Master"],"text":"Master is a HUGE DICK to Unfortunate."}
Revolt  = {"characters":["Tyrant","Conspirator"],"text":"Tyrant is plotted against by Conspirator"}
DaringEnterprise  = {"characters":["Leader","Adversary"],"objects":["Thing"],"text":"Leader takes Thing from Adversary by overpowering Adversary"}
Abduction  = {"characters":["Abductor","Abducted","Guardian"],"text":"Abductor takes Abducted from Guardian"}
Enigma = {"characters":["Interrogator","Seeker"],"objects":["Problem"],"text":"Interrogator poses a Problem to Seeker, giving Seeker a better ability to reach their goals."}
Obtaining = {"characters":["Solicitor","Adversary"],"objects":["Thing"],"text":"Solicitor wants Thing that Adversary has, but Adversary won't give it to Solicitor."}
RivalryofKin  = {"characters":["Preferred","Rejected","Object"],"text":"Preferred and Rejected are family who both desire Object and Object chooses Preferred."}
Madness = {"characters":["Madman","Victim"],"text":"Madman goes totally crazy and hurts Victim."}
Imprudence = {"characters":["Imprudent"],"objects":["Thing"],"text":"Imprudent has Thing, but through neglect or ignorance loses it."}
BetrayTrust = {"characters":["Lover","Revealer"],"text":"Revealer betrays the trust of Lover."}
Unrecognized = {"characters":["Slayer","Victim"],"text":"Though Slayer and Victim are kin, Slayer does not notice as they wrong Victim."}
SacrificeForIdeal = {"characters":["Hero","Creditor"],"objects":["Thing"],"text":"To be true to themself, Hero must sacrifice Thing to Creditor."}
SacrificeForKin = {"characters":["Hero","Kinsman","Creditor"],"text":"When Kinsman is in trouble with Creditor, Hero sacrifices themself to protect Kinsman."}
LostForPassion = {"characters":["Lover"],"objects":["Sacrifice","Passion"],"text":"Lover cares so much about Passion, that they are willing to give up Sacrifice. But in the process, Lover loses Passion as well!"}
Necessity = {"characters":["Hero","Beloved"],"objects":["Need"],"text":"Though Hero cares deeply for Beloved, Need makes it necessary for Hero to sacrifice Beloved."}
UnevenRivalry = {"characters":["Superior","Inferior"],"objects":["Thing"],"text":"Superior defeats Inferior, winning Thing."}
DiscoveryofDishonor = {"characters":["Discoverer","Guilty"],"text":"Discoverer discovers the wrongdoing committed by Guilty."}
ObstacleToLove = {"characters":["Lover","Beloved"],"objects":["Thing"],"text":"Thing becomes an obstacle for the love of Lover and Beloved."}
EnemyLoved = {"characters":["Lover","Hater","Enemy"],"text":"Lover loves Enemy and speaks to Hater who hates Enemy."}
Ambition = {"characters":["Ambitious","Adversary"],"objects":["Thing"],"text":"Ambitious desires Thing, but Adversary opposes Ambitious."}
MistakenJealousy = {"characters":["Jealous","Accomplice","Author"],"objects":["Thing"],"text":"Jealous falls victim to Author and becomes jealous of Thing, causing Jealous to conflict with Accomplice."}
ErroneousJudgment = {"characters":["Mistaken","Victim","Author","Guilty"],"text":"Mistaken falls victim to Author and passes judgment against Victim instead of rightfully against Guilty!"}
Remorse = {"characters":["Culprit","Victim","Interrogator"],"text":"Culprit has wronged Victim, and attempts to deny it to Interrogator."}
Recovery = {"characters":["Seeker","Found"],"text":"Seeker has been searching for Found and finally finds them."}
LossofKin = {"characters":["Slain","Kin","Executioner"],"text":"The killing of Slain by Executioner is witnessed by Slain's kin, Kin."}


sitchlist = [Supplication,Deliverance,CrimePursued,Pursuit,Disaster,Cruelty,Revolt,DaringEnterprise,
             Abduction,Enigma,Obtaining,RivalryofKin,Madness,Imprudence,BetrayTrust,Unrecognized,
             SacrificeForIdeal,SacrificeForKin,LostForPassion,Necessity,UnevenRivalry,DiscoveryofDishonor,
             ObstacleToLove,EnemyLoved,Ambition,MistakenJealousy,ErroneousJudgment,Remorse,Recovery,
             LossofKin]

#content lists
#For reference, those implemented include:
#Homestuck, Community, Kill La Kill, Adventure Time, Avatar, Marvel, Doctor Who,
#DC, Harry Potter, Buffy, Temeraire, Fairy Tales
Homestuck = {"names":["Dave","John","Rose","Jade","Dirk","Roxy","Jane","Jake"],
             "aspects":["knight","heir","seer","witch","prince","rogue","maid","page","mage","thief","sylph","bard"],
             "objects":["kernelsprite","alchemizer"],
             "locations":["paradox space","the battlefield","a time traveling comet"]}

Community = {"names":["Troy","Abed","Shirley","Annie","Britta","Chang","Pierce","Jeff"],
             "aspects":["obtuse","undiagnoseable","cloying","day-planner","rebellious","literally psychotic","asshole","liar"],
             "objects":["missing pen","Troy's monkey"],
             "locations":["a classroom","the study room","the dorms"]}

KillLaKill = {"names":["Ryuko","Nonon","Mako","Satsuki","Gamagoori","Inumuta","Sanageyama","Mikisugi"],
              "aspects":["transfer student","band leader","slacker","class president","discipline enforcer","data analyst","sports organizer"],
              "objects":["school uniform","scissor blade","dramatic nipples"],
              "locations":["corporate headquarters","school courtyard"]}

AdventureTime = {"names":["Finn","Jake","Bubblegum","Marceline","Rainicorn","Simon"],
                 "aspects":["hero","lich","magic dog","princess","vampire","wizard"],
                 "objects":["enchiridion","summoning ritual","glasses of nerdicon"],
                 "locations":["a dungeon","a treehouse","the ice kingdom"]}

Avatar = {"names":["Aang","Katara","Sokka","Toph","Zuko","Iroh","Azula","Appa"],
          "aspects":["avatar","healer","sarcastic guy","badass","banished prince","old bro","crazy bitch","sky bison"],
          "objects":["bending scroll","disguise","spirit water"],
          "locations":["the fire nation","the south pole","the earth nation"]}

Marvel = {"names":["Scott","Logan","Eric","Charles","Reed","Jonny","Susan","Ben","Tony","Bruce","Steve","Peter","Emma"],
          "aspects":["mutant","avenger","fantastic","inhuman","superhero","soldier","monster","uncanny","amazing","ultimate","astonishing"],
          "objects":["power armor","mutant gene","gamma radiation"],
          "locations":["the Avengers mansion","Xavier's school for gifted children"]}

DrWho = {"names":["Rose","Martha","Donna","Clara","Matt","David","Peter","Chris","Tom","Sarah","John","Rory","Amy"],
         "aspects":["doctor","nurse","impossible girl","girl who waited","war doctor"],
         "objects":["TARDIS","sonic screwdriver","timey wimey machine"],
         "locations":["Cardiff","the end of the world"]}

HarryPotter = {"names":["Harry","Hermione","Ron","Neville","Draco","Albus","Minerva","Severus","Tom"],
               "aspects":["boy who lived","prefect","headmaster","professor","dark lord","death eater"],
               "objects":["wand","deathly hallow","horcrux","time turner"],
               "locations":["Godric's Hollow","Hogwarts"]}

Buffy = {"names":["Buffy","Willow","Dawn","Xander","Giles","Angel","Spike","Anya"],
         "aspects":["slayer","witch","key","heart","watcher","vampire","vengeance demon","mom"],
         "objects":["tome","stake","scythe","spell"],
         "locations":["the Hellmouth","the magic shop"]}

DC = {"names":["Clark","Bruce","Diana","Hal","Arthur","J'onn","Kyle","Wally","Barry","Damien"],
      "aspects":["hero","warrior","green lantern","king","alien","hunter","flash"],
      "objects":["cape","cowl","lasso of truth","ring of power"],
      "locations":["Justice League headquarters","Atlantis","Gotham","Metropolis"]}

FairyTale = {"names":["Red Riding Hood","Cinderella","Snow White","Rapunzel","Jack","Aurora","Charming"],
             "aspects":["princess","huntsman","giant-killer","Prince","witch","baker"],
             "objects":["cow as white as milk","cape as red as blood","hair as yellow as corn","slipper as pure as gold"],
             "locations":["the woods","a tower in a glade","grandmother's house"]}

Temeraire = {"names":["Laurence","Granby","Rowland","Temeraire","Iskierka","Perscitia","Demane","Sipho","Lily","Maximus"],
             "aspects":["captain","dragon","imperial","admiral","lieutenant","runner","crewmember"],
             "objects":["mushroom","harness","pavilion"],
             "locations":["Dover","the Cape","the deck of a transport ship"]}






from random import *


#First we will create a story structure, one of the six structures from Booker


def SetStructure(story,genres):
    #populate the story with a structure
    story["structure"] = Monster
    #populate the name and aspect lists
    story["namelist"]=[]
    story["aspectlist"]=[]
    story["objectlist"]=[]
    for genre in genres:
        story["namelist"]+=genre["names"]
        story["aspectlist"]+=genre["aspects"]
        story["objectlist"]+=genre["objects"]
    #and build a list of scenes
    story["scenes"] = []
    story["characters"]=[]
    story["objects"]=[]
    for scene in story["structure"]:
        story["scenes"].append(NewScene(story,story["structure"][scene]))

def NewScene(story, scene, sitch=None):
    '''
    @input story is the story in which the scene will take place
    @input scene should be a dictionary with some requirements for the scene
    @optional sitch is a dramatic situation that can be selected or randomly generated
    @output is a string which fills in a template from @sitch with elements from @story
    '''

    sitch = choice(sitchlist)

    #add characters if there aren't enough for this scene
    while len(story["characters"]) <= len(sitch["characters"]):
        AddCharacter(story)
        
    #randomly select which characters from the story will play the roles in the situation
    roles = sample(story["characters"],len(sitch["characters"]))
    
    
    #write the text of the scene with the 
    ourscene = str(sitch["text"])
    for charind in range(0,len(sitch["characters"])):
        #needs better signifier selection
        ourscene = ourscene.replace(sitch["characters"][charind],roles[charind]["name"]+", the "+roles[charind]["class"]+",",1)
        ourscene = ourscene.replace(sitch["characters"][charind],roles[charind]["name"])
    if "objects" in sitch:
        while len(story["objects"]) <= len(sitch["objects"]):
            AddObject(story)
        shuffle(story["objects"])
        for objind in range(0,len(sitch["objects"])):
             ourscene = ourscene.replace(sitch["objects"][objind],story["objects"][objind])
    return ourscene



def AddCharacter(story):
    '''
    @input story the story to which a character will be added
    @optional genre a selection of what flavor the character will have
    '''
    #for now the character's name and class are fixed
    shuffle(story["namelist"])
    name = story["namelist"].pop()
    shuffle(story["aspectlist"])
    aspect = story["aspectlist"].pop()
    story["characters"].append({"name":name,"class":aspect})
    return

def AddObject(story):
    shuffle(story["objectlist"])
    story["objects"].append(story["objectlist"].pop())
    return

#begin with an empty story dictionary
Story = {}
SetStructure(Story,[Homestuck,Community,AdventureTime])
for scene in Story["scenes"]:
    print(scene)                  
                   
