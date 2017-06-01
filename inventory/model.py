import mongoengine as me


class Host(me.BaseDocument):
    host = me.StringField(primary_key=True)
    groups = me.ListField()
    variables = me.DynamicEmbeddedDocument()


class Group(me.BaseDocument):
    name = me.StringField(primary_key=True)
    hosts = me.ListField()
    children = me.ListField()
    variables = me.DynamicEmbeddedDocument()
