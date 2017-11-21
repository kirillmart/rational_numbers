class Animal:

    GENDERS = {
        "M": "male",
        "F": "female",
    }

    def __init__(self, color, gender, age, legs=4, name=None, tail=True):
        if not gender.upper() in Animal.GENDERS.keys():
            raise TypeError
        self.gender = gender.upper()
        self.color = color
        self.legs = legs
        self.age = age
        self.name = name
        self.tail = tail

    def __str__(self):
        return "<{}; Gender: {}; Color: {}>".format(
            self.__class__.__name__,
            self.gender,
            self.color
        )

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @staticmethod
    def static_method():
        return "static method"

    def __repr__(self):
        return "1 + 1"

    def voice(self):
        raise NotImplemented("Method is not implemented")

    @property
    def has_voice(self):
        return bool(self.voice())
