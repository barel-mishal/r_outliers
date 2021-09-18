class softwares:
    names = []
    versions = {}

    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")

    def __str__(self):
        s = "The current softwares and their versions are listed below: \n"
        for key, value in self.versions.items():
            s += f"{key} : v{value} \n"
        return s

    def __getitem__(self, name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")


p = softwares(['S1', 'S2', 'S3'])
# p1 = softwares([])

print(p['S2'])
