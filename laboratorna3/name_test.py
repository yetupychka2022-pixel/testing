class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Bohdan", "Anonim", "Yevhen"]:
            raise ValueError("Allowed names: Bohdan, Anonim, Yevhen")
        if hobby == "":
            raise ValueError("Hobby cannot be empty")
        self.name = name
        self.hobby = hobby

a = Name("Yevhen", "football")
print(a.name, a.hobby)
