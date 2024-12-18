class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors=[]):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _list_dependencies(self, dependencies):
        write = ""
        for item in dependencies:
            write += "\n- " + item
        return write

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'} \n"
            f"\nAuthors: {self._list_dependencies(self.authors)} \n"
            f"\nDependencies: {self._list_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._list_dependencies(self.dev_dependencies)}\n"
        )
