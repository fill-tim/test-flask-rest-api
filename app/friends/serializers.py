class FriendListSerializer:
    """ Сериализатор для списка друзей пользователя """
    def friend_serialize(self, friends):
        friend_dict = [self.serialize_f(obj) for obj in friends]
        return friend_dict

    def serialize_f(self, obj):
        return {
            "id": obj.id,
            "username": obj.username,
            "email": obj.email
        }
