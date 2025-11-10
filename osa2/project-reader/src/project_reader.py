from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
#        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tulos = toml.loads(content)["tool"]["poetry"]

        authors = []
        for key in tulos["authors"]:
            authors.append(key)

        dependencies = []
        for key in tulos["dependencies"]:
            dependencies.append(key)
        dev_dependencies = []
        for key in tulos["group"]["dev"]["dependencies"]:
            dev_dependencies.append(key)

        return Project(tulos["name"], tulos["description"], tulos["license"], authors, dependencies, dev_dependencies)
