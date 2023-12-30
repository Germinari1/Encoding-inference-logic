from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
db = Symbol("db")

knowledge = And(Implication(Not(rain), hagrid),
                Or(hagrid, db),
                Not(And(hagrid, db)),
                db)

print(model_check(knowledge, rain)) 

#print(knowledge.formula())