import os
import json
from typing import List

class ConfigurationService() : 

    _configurationData:any

    def __init__(self) -> None:
        self.ReadConfigurationFile()

    def ReadConfigurationFile(self) : 
        with open(os.path.join(os.getcwd(), 'Application', 'Configurations', 'Web.config.json'), 'r', encoding='utf-8') as configurationFile :
            self._configurationData = json.load(configurationFile)

    @property
    def SQLiteConnectionString(self) : 
        return 'sqlite:///' + os.path.join(os.getcwd(), 'Infrastructure', 'SQLite', 'db.db?check_same_thread=False')

    @property
    def FastApiTitle(self) : 
        return self._configurationData['fastApiTitle']

    @property
    def FastApiVersion(self) : 
        return self._configurationData['fastApiVersion']

    @property
    def FastApiDescription(self) : 
        return self._configurationData['fastApiDescription']

    @property
    def UvicornHost(self) : 
        return self._configurationData['uvicornHost']

        
    @property
    def UvicornPort(self) : 
        return self._configurationData['uvicornPort']

    @property
    def TokenSecretKey(self) : 
        return self._configurationData['tokenSecretKey']

    @property
    def TokenAlgorithm(self) -> List : 
        return self._configurationData['tokenAlgorithm']

        