

# Marvish Chandra
# This program is intended to determine the various factors of life expectancy.

class unhealthyPeople:

def __init__(self,unhealthyMale,unhealthyFemale):
    self.unhealthyMale = unhealthyMale
    self.unhealthyFemale = unhealthyFemale

    def printCouple(self):
        print(unhealthyMale,unhealthyFemale)

    def unfortunateMale(self):
        print(self.unhealthyMale + "will often likely to drink more, commit riskier activities, and die at a younger age than women.")

    def unfortunateFemale(self):
        print(self.unhealthyFemale + "will often likely gain too much weight, have a higher sugar intake, and suffer from a lack of exercise.")

class commonDiseases:

def varietyDiseases():
    sexualDiseases = {"Chlamydia": {0},"HIV":{1},"AIDS":{2},"Herpes":{3},"Gonorrhea":{4}}
    foodDiseases = {"Diabetes":{0},"E-coli":{1},"Salmonella":{2},"Norovirus":{3},"Influenza":{4},"Campylobacter":{5}}
    lungDiseases = {"Pneumonia":{0},"Asthma":{1},"Erectile Dysfunction":{2},"Ectopic Pregnancy":{3},"Acid Reflux":{4},"Tuberculosis":{5}}
    heartDiseases = {"Coronary Artery Disease":{0},"Arrhythmia":{1},"Cardiomyopathy":{2},"Heart Failure":{3},"Congenital":{4},"Atrial fibrillation":{5},"Myocarditis":{6},"Pericarditis":{7}, "High Blood Pressure":{8}}
    for s in sexualDiseases:
        for f in foodDiseases:
            for l in lungDiseases:
                for h in heartDiseases:
                    print(s,f,l,h)

class ageFactor:
    def ageRisk(age):
        if age > 20:print("You are at the prime age. You can enjoy being unhealthy, however, moderate everything you intake.")
        if age > 30:print("By this time, you are in the mid-level or senior level of your career. Be active when possible since you can't eat as much before.")
        if age > 40:print("You are at risk of arthritis and especially diabetes. Make sure to have a good diet, sleep, and enough exercise.")
        if age > 50:print("Obesity,hair loss, and cancer are the top problems you have by now. Take care of yourself and you must diet.")
        if age > 60:print("Cancer and stroke are your biggest problem at this age. Your diet affects stroke and how you walk. Cancer is unfortunately genetic.")
        if age > 70:print("Unfortunately, you may get osteoarthritis. Your joints become weaker and more frail. Be healthy and stay active.")
        if age > 80:print("You have maintained a healthy life if you've lived this long. This is the average age when most die.")


class badConsumption:

unhealthyFoods = ["Processed","Fried","Salty"]
for u in unhealthyFoods:
    print(u)

unhealthyDrinks = ["Carbonated","Alcoholic","Sports","Intake"]
for d in unhealthyDrinks:
    print (d)

