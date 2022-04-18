from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query))

    def hasAtLeast(self, number, category):
        return QueryBuilder(And(HasAtLeast(number, category), self.query))

    def hasFewerThan(self, number, category):
        return QueryBuilder(And(HasFewerThan(number, category), self.query))

    def oneOf(self, *args):
        return QueryBuilder(Or(*args))

    def build(self):
        return self.query
