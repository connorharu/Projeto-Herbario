import requests

class species_link():
    def __init__(self, api_key): # __init__ é como um construtor
        self.apikey = api_key # self é uma referencia a propria instancia da classe;
                              # api_key é o parametro que se espera receber ao instanciar a classe;

    # metadados básicos
    def get_metadata(self):
        url = "https://specieslink.net/ws/1.0/info"
        response = requests.get(url, params={"apikey": self.apikey}) # params recebe o parametro da URL da requisição HTTP GET
                                                                     # onde a chave é apikey e o valor é self.apikey
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter os metadados")
            return None

    # todas as coleções e instituições participantes
    def get_participants(self):
        url = "https://specieslink.net/ws/1.0/participants"
        response = requests.get(url, params={"apikey": self.apikey}) # params recebe o parametro da URL da requisição HTTP GET
                                                                     # onde a chave é apikey e o valor é self.apikey
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter as coleções e instituições participantes")
            return None

    # dados de uma instituição por sigla ou identificador
    def get_institution_data(self, identifier, lang=None): # lang = none inicialmente indica que é opcional
        url = f"https://specieslink.net/ws/1.0/ins/{identifier}/" # f-string deixa adicionar expressões
        params = {"apikey": self.apikey} # params é um dicionário; recebe o parametro da URL da requisição HTTP GET
                                         # onde a chave é apikey e o valor é self.apikey
        if lang:
            params["lang"] = lang # adicionando parametro lang ao dicionario params para filtragem
        response = requests.get(url, params=params) # HTTP GET para a URL requisitada passando os parametros
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter os dados da instituição")
            return None

    # dados de uma coleção por sigla ou identificador
    def get_collection_data(self, identifier, lang=None): # lang = none inicialmente indica que é opcional
        url = f"https://specieslink.net/ws/1.0/col/{identifier}/"  # f-string deixa adicionar expressões
        params = {"apikey": self.apikey} # params é um dicionário; recebe o parametro da URL da requisição HTTP GET
                                         # onde a chave é apikey e o valor é self.apikey
        if lang:
            params["lang"] = lang # adicionando parametro lang ao dicionario params para filtragem 
        response = requests.get(url, params=params)  # HTTP GET para a URL requisitada passando os parametros
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter os dados da coleção")
            return None
    
    # dados de um conjunto de dados com um identificador especifico
    def get_dataset_info(self, id_dataset):
        url = f"https://specieslink.net/ws/1.0/dts/{id_dataset}/"
        # não tem parâmetro lang
        response = requests.get(url, params={"apikey": self.apikey}) # params recebe o parametro da URL da requisição HTTP GET
                                                                     # onde a chave é apikey e o valor é self.apikey
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter informações do conjunto de dados")
            return None
    
    # busca por registros de biodiversidade
    def search_records(self, filters): # tem os filtros requisitados como parâmetro
        url = "https://specieslink.net/ws/1.0/search"
        params = {"apikey": self.apikey} # params recebe o parametro da URL da requisição HTTP GET
                                         # onde a chave é apikey e o valor é self.apikey
        params.update(filters)  # adiciona os filtros fornecidos ao dicionário de parâmetros
        response = requests.get(url, params=params) # HTTP GET para a URL requisitada passando os parametros
        if response.status_code == 200: # solicitação feita com sucesso se ACK HTTP = 200
            data = response.json()
            return data
        else:
            print("erro ao obter os registros de biodiversidade")
            return None