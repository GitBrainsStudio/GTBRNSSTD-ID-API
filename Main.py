from Startup.DependenciesService import DependenciesService


class Main() : 

    _dependenciesService:DependenciesService = DependenciesService()

    _dependenciesService.RegisterControllers()
    _dependenciesService.UvicornService.RunApi()

Main()