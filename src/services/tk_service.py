class TKService:
    """Luokka, joka säilyttää tiliin liittyviä tietoja ennen pysyvää tallennusta

    Atrributes:
        name: Tilin nimi
        money_in: Sanakirja, joka sisältää tilille saapuvat tapahtumat
        money_out: Sanakirja, joka sisältää tililtä lähtevät tapahtumat
        offset_account_in: Sanakirja, joka sisältää tilille saapuvien tilitapahtumien luokittelun
        offset_account_out: Sanakirja, joka sisältää tililtä lähtevien tilitapahtumien luokittelun
        self_loans: Sanakirja, joka sisältää tilin lainaksi luokitellut tapahtumat
        self_interests: Sanakirja, joka sisältää lainojen korot
    """

    def __init__(self, name:str):
        """Luokan konstruktori, joka luo uuden tiliolion

        Args:
            name: Tilin nimi
    """
        self.name = name
        self.money_in = {}
        self.money_out = {}
        self.offset_account_in = {}
        self.offset_account_out = {}
        self.loans = {}
        self.interests = {}

    def summary(self, info:str):
        """Toiminto, joka lukee käyttäjän antaman tiliotteen ja jakaa tapahtumat
            tilille tuleviin ja tililtä lähteviin tapahtumiin

        Args: 
            info: Tilitiedoston polku ja nimi
        """
        with open(info, "rt", encoding = "utf_8") as file:
            lines = file.readlines()
        for line in lines[1:]:
            line = line.split(";")
            amount = float(line[1].replace(",", "."))
            if amount < 0:
                if line[5] not in self.money_out:
                    self.money_out[line[5]] = 0
                self.money_out[line[5]] += amount
            else:
                if line[5] not in self.money_in:
                    self.money_in[line[5]] = 0
                self.money_in[line[5]] += float(amount)
