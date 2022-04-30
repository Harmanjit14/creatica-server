import graphene
from sentiment_analysis.sentiment import sentiment_scores

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    analysis = graphene.String(message=graphene.String(required=True))

    def resolve_analysis(self, info, message):
        return sentiment_scores(message)


schema = graphene.Schema(query=Query)
