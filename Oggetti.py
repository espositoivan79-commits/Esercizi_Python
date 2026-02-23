"""class Studente:
    def __init__(self, nome, eta, codice_studente):
        self.nome = nome
        self.eta = eta
        self.__codice_studente = None
        self.set_codice_studente(codice_studente)
    def get_codice_studente(self):
        return self.__codice_studente
    
    def set_codice_studente(self, nuovo_codice):
        if nuovo_codice.startswith("S") and len(nuovo_codice) == 8:
            self.__codice_studente = nuovo_codice
        else:
            print("Errore: il codice deve iniziare con la 'S' e avere 8 caratteri.")

    def descrizione(self):
        return f"{self.nome} ha {self.eta} anni."
studente1 = Studente("Ivan", 46, "S1234567")
print(studente1.get_codice_studente())

studente1.set_codice_studente("S7654321")
print(studente1.get_codice_studente())

studente1.set_codice_studente("S1276543")"""


"""class Studente:
    def __init__(self, nome, eta, cod_stud):
        self.nome = nome
        self.eta = eta
        self.cod_stud = cod_stud
    
    def descrizione(self):
        return f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.cod_stud}"
    
    def tipo_studente(self):
        return "Studente generico"

class StudenteUniversitario(Studente):
    def __init__(self, nome, eta, cod_stud, corso_di_laurea):
        super().__init__(nome, eta, cod_stud)
        self.corso_laurea = corso_di_laurea
    
    def descrizione(self):
         return f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.cod_stud}, Corso: {self.corso_laurea}"
    
    def tipo_studente(self):
        return "Studente universitario"

class StudenteLiceale(Studente):
    def __init__(self, nome, eta, cod_stud, indirizzo):
        super().__init__(nome, eta, cod_stud)
        self.indirizzo = indirizzo 
    
    def descrizione(self):
         return f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.cod_stud}, Indirizzo: {self.indirizzo}"
    
    def tipo_studente(self):
        return "Studente liceale"
    
#Creazione degli oggetti
studente_generico = Studente("Ivan", 46, "S9584732")
studente_leceale = StudenteLiceale("Grazia", 50, "S8954236", "Liceo classico")
studente_universitario = StudenteUniversitario("Ale", 26, "S4578129", "Ingegneria informatica")

studenti = [studente_generico, studente_leceale, studente_universitario]

for studente in studenti:
    print(studente.descrizione())
    print(f"Tipo di studente: {studente.tipo_studente()}\n")"""


"""class Studente:
    def __init__(self, nome, eta, cod_stud):
        self.nome = nome
        self.eta = eta
        self.cod_stud = cod_stud
    
    def descrizione(self):
        descrizione = f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.cod_stud}"
    
        if hasattr(self, "corso_laurea"):
            descrizione += f", Corso: {self.corso_laurea}"
        
        if hasattr(self, "indirizzo"):
            descrizione += f", Indirizzo: {self.indirizzo}"
    
        return descrizione
    
    def tipo_studente(self):
        return "Studente generico"

class StudenteUniversitario(Studente):
    def __init__(self, nome, eta, cod_stud, corso_di_laurea):
        super().__init__(nome, eta, cod_stud)
        self.corso_laurea = corso_di_laurea
    
    def tipo_studente(self):
        return "Studente universitario"

class StudenteLiceale(Studente):
    def __init__(self, nome, eta, cod_stud, indirizzo):
        super().__init__(nome, eta, cod_stud)
        self.indirizzo = indirizzo 
    
    
    def tipo_studente(self):
        return "Studente liceale"
    
#Creazione degli oggetti
studente_generico = Studente("Ivan", 46, "S9584732")
studente_leceale = StudenteLiceale("Grazia", 50, "S8954236", "Liceo classico")
studente_universitario = StudenteUniversitario("Ale", 26, "S4578129", "Ingegneria informatica")

studenti = [studente_generico, studente_leceale, studente_universitario]

for studente in studenti:
    print(studente.descrizione())
    print(f"Tipo di studente: {studente.tipo_studente()}\n")"""
    

class Studente:
    def __init__(self, nome, eta, cod_stud):
        self.nome = nome
        self.eta = eta
        self.cod_stud = cod_stud
    
    def descrizione(self):
        return f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.cod_stud}{self.extra()}"

    def extra(self):
        return ""
        
    def tipo_studente(self):
        return "Studente generico"

class StudenteUniversitario(Studente):
    def __init__(self, nome, eta, cod_stud, corso_di_laurea):
        super().__init__(nome, eta, cod_stud)
        self.corso_di_laurea = corso_di_laurea
    
    def extra(self):
        return f", Corso di laurea: {self.corso_di_laurea}"

    def tipo_studente(self):
        return "Studente universitario"

class StudenteLiceale(Studente):
    def __init__(self, nome, eta, cod_stud, indirizzo):
        super().__init__(nome, eta, cod_stud)
        self.indirizzo = indirizzo 
    
    def extra(self):
        return f", Indirizzo: {self.indirizzo}"

    def tipo_studente(self):
        return "Studente liceale"
    
#Creazione degli oggetti
studente_generico = Studente("Ivan", 46, "S9584732")
studente_leceale = StudenteLiceale("Grazia", 50, "S8954236", "Liceo classico")
studente_universitario = StudenteUniversitario("Ale", 26, "S4578129", "Ingegneria informatica")

studenti = [studente_generico, studente_leceale, studente_universitario]

for studente in studenti:
    print(studente.descrizione())
    print(f"Tipo di studente: {studente.tipo_studente()}\n")