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
      }
```	

## Ohjelman pakkausrakenne

Ohjelma on pakattu toimintoja kuvaaviin kansioihin. UI-kansiossa on käyttöliittymä ja käyttöliittymää
lähellä olevat kyselyt/toiminnot. Service-kansiossa on sovelluslogiikka ja Repositories-kansiossa on 
ohjelman pysyväistallennuksesta vastaavat toiminnot. 

![Pakkausrakenne](./kuvat/pakkaus.jpg)

## Päätoiminnallisuus

Ohjelmassa tällä hetkellä olevat toiminnot ovat tiedoston lisääminen, kassavirtalaskelman tulostus, tuloslaskelman tulostus, tilitietojen
haku ja tilien yhdistäminen. Ohjelman käyttö edellyttää aluksi tilitiedoston lisäämistä. Ohjelma pyytää käyttäjää luokittelemaan tilitapahtumat
ja tämän jälkeen tilitiedot tallennetaan pysyväismuistiin. Toistaiseksi kassavirtalaskelman ja tuloslaskelman tulostus tapahtuu tilapäisesti
tallennettujen tietojen varassa. Tilitietojen haku ja tilien yhdistäminen perustuu pysyväisesti tallennettuun tietoon. Tilitietoja voi tällä
hetkellä hakea tilitapahtuman nimen perusteella. Jos useampia tilejä on tallennettu, näiden tiedot on mahdollista yhdistää. Yhdistämisen
jälkeen tapahtumahaussa näkyy muiden tilien joukossa tili Yhdistetty, josta voi hakea tilitapahtumia samaan tapaan kuin muiltakin tileiltä.

### Ohjelman käynnistyminen

```mermaid
sequenceDiagram
   actor User
   participant UI
   participant Service
   participant Repositories
   UI->>User: "Valitse toiminto: "
   User->>UI: "1"
   UI-->UI: get_file()
   UI->>User: "Anna tiedosto: "
   User->>UI: "src/short.csv"
   UI->>UI: check_file("src/short.csv")
   UI-->UI: "True"
   UI->>User: "Anna tilille nimi: "
   User->>UI: "Nordea"
   UI-->UI: ("src/short.csv", "Nordea")
   UI->>UI: process_file("src/short.csv", "Nordea")
   UI->>Service: account = TKService("src/short.csv", "Nordea")
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
   actor USER
   participant UI.tui
   Participant UI.queries
   participant Service
   participant Repositories
   UI.tui->>User: "Valitse toiminto: "
   User-->UI.tui: "4"
   UI.tui->>UI.queries: search_events_by_name()
   UI.queries->>Repositories: get_account_names()
   Repositories-->UI.queries: accounts
   UI.queries->>USER: "Voit etsiä tapahtumia seuraavilta tileiltä: 1: Matti 2: Maija. Valintasi: "
   USER-->UI.queries: "2"
   UI.queries->>USER: "Valittu tili: Maija. Anna tapahtuman nimi: "
   USER-->UI.queries: "eli"
   UI.queries-->USER: "3/2022 Elisa 29.50 \n 4/2022 Elisa 32.50 \n Yhteensä 62.00"
   UI.queries->>USER: "Valitse: Uusi haku samalta tililtä (1) tai Takaisin päävalikkoon (2): "
   USER-->UI.queries: "2"
   UI.queries-->UI.tui: return
   UI.tui->>User: "Valitse toiminto: "
   User->>UI.tui: "6"
   UI.tui->>UI.tui: exit()
```
   
   
   


