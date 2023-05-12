# Kuvaus arkkitehtuurista

## Ohjelman rakenne

Ohjelma koostuu käyttöliittymästä, sovelluslogiikasta ja pysyväistallennuksesta. Käyttöliittymän
alaisuudessa on toimintoja, jotka luonteeltaan ovat käyttöliittymän ja sovelluslogiikan välimaastosta,
sisältäen kuitenkin enemmän käyttöliittymän tyyppisiä toimintoja. 

Sovelluslogiikka käsittelee käyttöliittymän kautta saatuja tietoja ja prosessoi ne muotoon, josta
pysyväistallennuksen kerros saa helposti tallennukseen tarvittavat tiedot. 


```mermaid
  classDiagram
      class TKService{
          name
	  	  money_in
          money_out
          offset_account_in
          offset_account_out
          self.loans
          self.interests
      }
```	

## Ohjelman pakkausrakenne

Ohjelma on pakattu toimintoja kuvaaviin kansioihin. UI-kansiossa on käyttöliittymä ja käyttöliittymää
lähellä olevat kyselyt/toiminnot. Service-kansiossa on sovelluslogiikka ja Repositories-kansiossa on 
ohjelman pysyväistallennuksesta vastaavat toiminnot. 

![Pakkausrakenne](./kuvat/pakkaus.jpg)

## Päätoiminnallisuus

Ohjelmassa tällä hetkellä olevat toiminnot ovat S-Pankin ja Nordean tiliotetiedoston lisääminen, tilitapahtumien etsiminen ja raporttien tulostaminen sekä tilien yhdistäminen.

Ohjelman käyttö edellyttää aluksi tilitiedoston lisäämistä. Ohjelma pyytää käyttäjää luokittelemaan tilitapahtumat ja tämän jälkeen tilitiedot tallennetaan pysyväismuistiin. Tilitiedoston tallennuksen jälkeen kaikki toiminnot perustuvat pysyväisesti tallennettuun tietoon. Tilitietoja voi hakea tilitapahtuman nimen perusteella. Tulostettavien raporttien vaihtoehdot ovat tuloslaskelma, kassavirtalaskelma ja muutokset tase-erissä. Jos useampia tilejä on tallennettu, näiden tiedot on mahdollista yhdistää. Yhdistämisen jälkeen yhdistetylle tilille on käytössä samat toiminnot kuin muillekin tileille.

### Ohjelman käynnistyminen

```mermaid
sequenceDiagram
   actor User
   participant UI
   participant Service
   participant Repositories
   UI->>User: "Valitse toiminto: "
   User->>UI: "1"
   UI-->UI: get_file("Nordea")
   UI->>User: "Anna tiedosto: "
   User->>UI: "Nordea.csv"
   UI->>UI: check_file("Nordea.csv", "Nordea")
   UI->>Repositories: check_file_format("Nordea.csv", "Nordea")
   Repositories-->UI: True
   UI-->UI: "True"
   UI->>User: "Anna tilille nimi: "
   User->>UI: "Pekka Python"
   UI-->UI: ("Nordea.csv", "Pekka Python")
   UI->>UI: process_file("Nordea.csv", "Pekka Python")
   UI->>Service: account = TKService("Nordea.csv", "Pekka Python")
   UI->>Service: account.summary(account.path)
   UI->>UI: ui.quiries.choose_offset_account(account)
   UI->>User: kyselee
   User->>UI: vastailee
   UI->>Repositories: repositories.save_data.save_account(account)
   Repositories-->UI: "True"
   UI-->UI: "account"
   UI->>User: "Valitse toiminto: "
   User->>UI: "6"
   UI->>UI: exit()
```

### Tilitapahtumien haku

```mermaid
sequenceDiagram
   actor User
   participant UI.tui
   Participant UI.queries
   participant Service
   participant Repositories
   UI.tui->>User: "Valitse toiminto: "
   User-->UI.tui: "4"
   UI.tui->>UI.queries: search_events_by_name()
   UI.queries->>Repositories: get_account_names()
   Repositories-->UI.queries: accounts
   UI.queries->>User: "Valitse tili, jolta haluat etsiä tapahtumia. Valintasi (Matti/Maija): "
   User-->UI.queries: "Maija"
   UI.queries->>User: "Valittu tili: Maija. Anna tapahtuman nimi: "
   User-->UI.queries: "eli"
   UI.queries-->User: "3/2022 Elisa 29.50 \n 4/2022 Elisa 32.50 \n Yhteensä 62.00"
   UI.queries->>User: "Valitse: Uusi haku samalta tililtä (1) tai Takaisin päävalikkoon (2): "
   User-->UI.queries: "2"
   UI.queries-->UI.tui: return
   UI.tui->>User: "Valitse toiminto: "
   User->>UI.tui: "6"
   UI.tui->>UI.tui: exit()
```
   
   
   


