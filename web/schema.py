import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    analysis = graphene.String(message=graphene.String(required=True))

    def resolve_analysis(self, info, message):
        return 


schema = graphene.Schema(query=Query)
