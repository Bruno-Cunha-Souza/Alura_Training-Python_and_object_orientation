from abc import ABC #abstract base classes

# Mother Class
class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes
    
    @property
    def name(self):
        return self._name
        
    def liker(self):
        self._likes += 1
    
    @name.setter
    def name(self, new_name):
        self._name =  new_name.title()
        
    def __str__(self):
        return f'{self._name}: \nlançado em {self.year} \n{self.likes} Likes\n'

# Class Filmes
class Filme (Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
    def __str__(self):
       return f'{self._name}: \nlançado em {self.year} \n{self.duration} min\n{self.likes} Likes\n'

# Class Series             
class Serie (Program):
    def __init__(self, name, year, season):
        super().__init__(name, year) 
        self.season = season
    def __str__(self):
        return f'{self._name}: \nlançado em {self.year} \n{self.season} temporadas\n{self.likes} Likes\n'

# Class Playlist 
class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs
       
    def __getitem__ (self, item):
        return self._programs[item]
        
    @property
    def listing(self):
        return self._programs
    
    
    def __len__(self):
      return len(self._programs)  
        
    
                  
avengers = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 199, 123)
arcane = Serie('Arcane', 2021, 1)

avengers.liker()
tmep.liker()
tmep.liker()
arcane.liker()
arcane.liker()
arcane.liker()
arcane.liker()
atlanta.liker()
atlanta.liker()

print('---------------------------------------------------')
print('---------------------------------------------------\n')

series_and_filmes = [avengers, atlanta, arcane, tmep]
playlist_rlx = Playlist('Relaxar', series_and_filmes)

print(f'Numero de itens na playlist é: {len(playlist_rlx)} \n')

for program in playlist_rlx:
    print(program)
    
print('\n---------------------------------------------------')   