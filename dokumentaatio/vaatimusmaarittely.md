# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjää muodostamaan kuva omasta taloudellisesta tilanteesta. Sovelluksella on vain
yksi käyttäjä ja sovellus tulkitsee kaikki saamansa tiedot saman käyttäjän antamiksi. 

## Suunnitellut toiminnot

Sovelluksen toiminta pohjautuu käyttäjän antamaan CSV-muotoiseen tiedostoon, jossa on tilitapahtumat halutulta ajanjaksolta.
Tämän pohjalta luodaan yhteistyössä käyttäjän kanssa tilikartta, joka palvelee käyttäjän tarpeita. Sovellus muodostaa
tilitapahtumien pohjalta kassavirtalaskelman ja tuloslaskelman sekä taseen tilikauden päättyessä. 

## Perusversion tarjoama toiminnallisuus

Ensimmäisessä vaiheessa toteutetaan versio, joka pyytää käyttäjältä Nordean tilitapahtumista muodostetun CSV-tiedoston.
Käyttäjälle tarjotaan mahdollisuutta antaa pankkitilin saldo tilikauden alkua edeltävänä päivänä. Tilikartta pidetään
minimissä: tuloslaskelman ainoat tilit ovat Tulot ja Menot ja vastaavasti taseen ainoa tili on Varat. Käyttäjä pääsee
tässä vaiheessa ainoastaan näkemään, paljonko rahaa on tullut ja mennyt. Sovellus tulostaa raportit tietokoneen
näytölle tekstinä.

## Perusversion jälkeen lisättävät toiminnallisuudet

Kun ohjelmasta on saatu toimiva perusversio, laajennetaan toiminnallisuuksia, jotta sovelluksesta olisi jotain hyötyäkin.
Toiminnallisuuksia on tarkoitus lisätä sen verran, mitä aikataulu sallii ja osa listalla olevista toiminnallisuuksista on
pikemminkin optimistisia tulevaisuuden visioita realistisia tavoitteita, joita ehtisi toteuttaa kurssin aikataulun
puitteissa.

 - Ohjataan käyttäjää laatimaan tilikartta, joka palvelee hänen tarkoituksiaan. Käydään tilitapahtumat läpi ja pyydetään
   käyttäjää valitsemaan niille sopivat vastatilit (esim. sähkölasku merkitään asumismenoksi). 
 - Tarjotaan mahdollisuus lisätä taseeseen opintolaina tai asuntolaina ja tähän liittyen tarjotaan mahdollisuutta
   pilkkoa lainanhoitoon liittyvät tilitapahtumat korkomenoihin ja lainanlyhennyksiin.
 - Tarjotaan mahdollisuus kyselyihin. Voidaan hakea esim. asumismenot halutulta ajalta tai näyttää vuoden ruokamenot
   kuukausittain.
 - Tarjotaan mahdollisuutta käyttää myös muista pankeista tulostettuja CSV-tiedostoja ja ohjeistetaan käyttäjä
   muokkaamaan tiedosto muotoon, josta sovellus löytää tarvitsemansa tiedot. 
 - Tarjotaan mahdollisuus lisätä tase-eriä, joista voidaan tehdä tasapoistoja, esim. kodinkoneet ja huonekalut. Näiden
   tarkoitus on auttaa käyttäjää hahmottamaan, kuinka paljon kuukaudessa pitäisi jäädä säästöön, jotta huonekaluja ja
   kodinkoneita on varaa uusia tarpeen mukaan ilman osamaksuja.
 - Tarjotaan mahdollisuus syöttää yksittäisiä käteisostoksia käyttöliittymän kautta.
 - Tarjotaan mahdollisuus lisätä tasetileihin useampia pankkitilejä. 
 - Lisätään tulostuksiin yksinkertaista grafiikkaa, joka helpottaa kokonaisuuden hahmottamista.

## Toimintaympäristön rajoitteet

Sovellus toimii Linux-käyttöjärjestelmällä varustetuissa koneissa. Sovellus tallennetaan käyttäjän koneelle ja se
käyttää myös käyttäjän koneen tallennustilaa tietokantatiedostojen tallennukseen.
