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

Ohjelman toiminnallisuudet rajoittuvat tällä hetkellä tilapäistallennettujen tietojen käyttöön. Ohjelma tallentaa tietoja
pysyväistiedostoon, mutta näitä tietoja ei päästä vielä käyttämään. Kuvataan tämänhetkistä toimintaa ohjelman käynnistyessä.

### Ohjelman käynnistyminen

```mermaid
sequenceDiagram
   actor User
   participant UI
   participant Services
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
   User->>UI: "4"
   UI->>UI: exit()
```


