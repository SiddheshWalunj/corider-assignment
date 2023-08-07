import mongoengine as me

class UserDetailTable(me.Document):
    name = me.StringField()
    email = me.StringField()
    password = me.BinaryField()

    meta = {
        'collection': 'user_data'
    }
