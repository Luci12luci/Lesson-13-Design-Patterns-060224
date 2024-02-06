# class Singleton:
#     _instance = None
#
#     def __init__(self):
#         if Singleton._instance is not None:
#             raise Exception("Tato trieda je Singleton a uz bola instancovana!")
#         else:
#             self.meno = "Patrik"
#             Singleton._instance = self
#
#     @staticmethod
#     def getInstance():
#         if Singleton._instance is None:
#             Singleton()
#         return Singleton._instance
#
# s1 = Singleton.getInstance()
# print(s1.meno)
# s2 = Singleton.getInstance()
# s1.meno = "Milan"
# print(s2.meno)
# s3 = Singleton()
# s1.meno = "Peter"
# print(s3.meno)

# FACTORY METHOD

# class Document:
#    def create(self):
#        raise NotImplementedError("Metoda create() musi byt prepisana.")
#
# class PDFDocument(Document):
#     def create(self):
#         return "Vytvaram PDF dokument."
#
# class WordDocument(Document):
#     def create(self):
#         return "Vytvaram Word dokument."
#
# class TXTDocument(Document):
#     def create(self):
#         return "Vytvaram TXT dokument."
#
# class Factory:
#     def create_document(self, type):
#         if type == "pdf":
#             return PDFDocument()
#         elif type == "word":
#             return WordDocument()
#         elif type == "txt":
#             return TXTDocument()
#         else:
#             raise ValueErro("Neznamy typ dokumentu")
#
# factory = Factory()
# pdf = factory.create_document("pdf")
# print(pdf.create())
#
# word = factory.create_document("word")
# print(word.create())
#
# txt = factory.create_document("txt")
# print(txt.create())


# BUILDER METHOD
# class Form:
#     def __init__(self):
#         self.fields = []
#
#     def add_field(self, field):
#         self.fields.append(field)
#
#     def __str__(self):
#         return "\n".join(self.fields)
#
# class FormBuilder:
#     def __init__(self):
#         self.form = Form()
#
#     def add_name_field(self):
#         self.form.add_field("Name: [______] ")
#         return self
#
#     def add_address_field(self):
#         self.form.add_field("Address: [______] ")
#         return self
#
#     def add_email_field(self):
#         self.form.add_field("Email: [_______] ")
#         return self
#
#     def build(self):
#         return self.form
#
# builder = FormBuilder()
# form = builder.add_name_field().add_address_field().add_email_field().build()
# print(form)

# DEKORATOR

class Napoj:
    def cena(self):
        raise NotImplementedError

class Kava(Napoj):
    def cena(self):
        return 2

class Caj(Napoj):
    def cena(self):
        return 3

class PrisadaDekorator(Napoj):
    def __init__(self, napoj):
        self._napoj = napoj

    def cena(self):
        return self._napoj.cena()

class Mlieko(PrisadaDekorator):
    def cena(self):
        return self._napoj.cena() + 5

class Cukor(PrisadaDekorator):
    def cena(self):
        return self._napoj.cena() + 2

moja_kava = Kava()
moja_kava = Mlieko(moja_kava)
moja_kava = Cukor(moja_kava)
print(moja_kava.cena())

moj_caj = Caj()
moj_caj = Cukor(moj_caj)
print(moj_caj.cena())

# OBSERVER

class AkciovaBurza:
    def __init__(self):
        self._investori = []
        self._cena_akcie = None

    def pridaj_investora(self, investor):
        self._investori.append(investor)

    def odstran_investora(self, investor):
        self._investori.remove(investor)

    def notifikuj_investorov(self):
        for investor in self._investori:
            investor.update(self._cena_akcie)

    def set_cena_akcie(self, cena):
        self._cena_akcie = cena
        self.notifikuj_investorov()

class Investor:
        def update(self, cena):
            print(f"Aktualizovana cena akcie: {cena}")

burza = AkciovaBurza()
investor1 = Investor()
investor2 = Investor()
investor3 = Investor()

burza.pridaj_investora(investor1)
burza.pridaj_investora(investor2)
burza.pridaj_investora(investor3)

burza.set_cena_akcie(100)
