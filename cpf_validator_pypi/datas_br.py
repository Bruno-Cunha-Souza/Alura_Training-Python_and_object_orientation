from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
           "", "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month 
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda-feira", "terça-feira",
            "quarta-feira", "quinta-feira", "sexta-feira",
            "sábado-feira", "domingo-feira"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime(" %d/%m/%Y \n %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro