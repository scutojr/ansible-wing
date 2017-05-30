import mongoengine as me


class Host(me.BaseDocument):
    groups = me.ListField()
    variables = me.DynamicEmbeddedDocument()


class Group(me.BaseDocument):
    hosts = me.ListField()
    children = me.ListField()
    variables = me.DynamicEmbeddedDocument()
