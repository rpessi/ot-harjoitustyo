# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjää muodostamaan kuva omasta taloudellisesta tilanteesta. Sovelluksella on vain yksi käyttäjä ja sovellus tulkitsee kaikki saamansa tiedot saman käyttäjän antamiksi. Sovellusta voi käyttää siihen, että yhdistää omia tilitietojaan useammalta tililtä tai siihen, että yhdistää perheenjäsenten tilit, jotta saadaan luotua kuva perheen taloudellisesta tilanteesta.

## Perusversion tarjoama toiminnallisuus

Sovelluksen toiminta pohjautuu käyttäjän antamaan CSV-muotoiseen tiedostoon, jossa on tilitapahtumat halutulta ajanjaksolta. Ohjelma pystyy käsittelemään Nordean ja S-Pankin csv-muotoisia tiliotteita. 

Ohjelma pyytää käyttäjää luokittelemaan tiliotteella näkyvät tapahtumat. Luokittelussa käytetyt luokat ovat: Tulot, Menot, Oma tili, Lainat. Kun käyttäjä luokittelee tapahtuman lainaksi, ohjelma kysyy korkojen määrää. Lainatapahtumat jaetaan korkoon ja lyhennykseen käyttäjältä saadun tiedon perusteella.

Tallennetuista tiedoista pystyy hakemaan tapahtumia nimellä yhdeltä tililtä kerrallaan. Tallennetuista tiedoista voi tulostaa myös raportteja: tuloslaskelma, kassavirtalaskelma ja muutokset tase-erissä. Raporttien sisältöä ja niiden tulkintaa on kuvailtu käyttöohjeessa tarkemmin. 

Ohjelmaan voi tallentaa useampia tilejä ja siinä on myös toiminto tilitietojen yhdistämiseen. Tallennetut tilit voidaan yhdistää yhdeksi ja tämän jälkeen tili Yhdistetty näkyy yhtenä vaihtoehtona, kun halutaan etsiä tapahtumia tililtä tai tulostaa raportti. Muut tallennetut tilit jäävät edelleen näkyviin omina tileinään.

## Jatkokehitysideoita

 - Ohjataan käyttäjää laatimaan tilikartta, joka palvelee hänen tarkoituksiaan. Käydään tilitapahtumat läpi ja pyydetään
   käyttäjää valitsemaan niille sopivat vastatilit (esim. sähkölasku merkitään asumismenoksi). 
 - Tarjotaan mahdollisuus laajempiin kyselyihin. Voidaan hakea esim. asumismenot halutulta ajalta tai näyttää vuoden ruokamenot
   kuukausittain.
 - Tarjotaan mahdollisuutta käyttää myös muista pankeista tulostettuja CSV-tiedostoja ja ohjeistetaan käyttäjä
   muokkaamaan tiedosto muotoon, josta sovellus löytää tarvitsemansa tiedot.
 - Tarjotaan mahdollisuus lisätä tase-eriä, joista voidaan tehdä tulosvaikutteisia tasapoistoja, esim. kodinkoneet ja 
   huonekalut. Näiden tarkoitus on auttaa käyttäjää hahmottamaan, kuinka paljon kuukaudessa pitäisi jäädä säästöön, jotta
   huonekaluja ja kodinkoneita olisi varaa uusia tarpeen mukaan ilman osamaksuja.
 - Mahdollisuus lisätä taseeseen luottokortti, jonka tapahtumat saadaan syötettyä PDF-tiedostosta.
 - Mahdollisuus lisätä taseeseen sijoituksia ja mahdollisuus päivittää näiden arvoja. Tähän liittyen lisättäisiin taseeseen
   tilit Sijoitusten käyvän arvon muutos ja Piilevä verovelka.
 - Mahdollisuus laskea erilaisia omaa taloutta kuvaavia tunnuslukuja tilikaudelta.

## Toimintaympäristön rajoitteet

Sovellus toimii Linux-käyttöjärjestelmällä varustetuissa koneissa. Sovellus tallennetaan käyttäjän koneelle ja se käyttää myös käyttäjän koneen tallennustilaa tilitietojen pysyväistallennukseen.
