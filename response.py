import random

payoff = { ("loyal", "loyal"): 3,
           ("loyal", "defect"): -5,
           ("defect", "defect"): 1,
           ("defect", "loyal"): 9 }

class Person:
    def __init__(self, defectresp, loyalresp):
        self.dr = max(.01, min(.99, defectresp))
        self.lr = max(.01, min(.99, loyalresp))
        self.wealth = 0.0
    

    def play(self, opplastmove):
        choice = random.random()
        if opplastmove == "defect":
            if self.dr > choice:
                return "loyal"
            else:
                return "defect"
        else:
            if self.lr > choice:
                return "loyal"
            else:
                return "defect"

    def mutate(self):
       return Person(self.dr + random.uniform(0.01, -.01),
                     self.lr + random.uniform(0.01, -.01))

    def clone(self):
        return Person(self.dr, self.lr)

    def __str__(self):
        return "Person(%g, %g, %g)" % (self.dr, self.lr, self.wealth)

# create a 50/50 person
p = Person(.5, .5)
populations = [ p.mutate() for _ in range(100) ]

# repeatedly:
#   mutate them into many populations
#   have those populations play each other
#   find the top 2 populations
for i in range(1000):
    for p in populations:
        one = p.clone()
        other = p.clone()
        lmone = "loyal"
        lmother = "loyal"
        for _ in range(1000):
            lmone, lmother = one.play(lmother), other.play(lmone)
            one.wealth += payoff[lmone, lmother]
            other.wealth += payoff[lmother, lmone]
        p.wealth = one.wealth + other.wealth
        

    populations.sort(key=lambda x: x.wealth)
    winner = populations[-1]
    print(winner)
    populations = [ winner.mutate() for _ in range(100) ]
# print out the ending defect responses and loyalty response probabilities
