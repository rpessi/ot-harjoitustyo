# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjää muodostamaan kuva omasta taloudellisesta tilanteesta. Sovelluksella on vain
yksi käyttäjä ja sovellus tulkitsee kaikki saamansa tiedot saman käyttäjän antamiksi. 

## Suunnitellut toiminnot

Sovelluksen toiminta pohjautuu käyttäjän antamaan CSV-muotoiseen tiedostoon, jossa on tilitapahtumat halutulta ajanjaksolta.
Tämän pohjalta luodaan yhteistyössä käyttäjän kanssa tilikartta (ei tehty), joka palvelee käyttäjän tarpeita. Sovellus muodostaa
tilitapahtumien pohjalta kassavirtalaskelman (tehty) ja tuloslaskelman (tehty) sekä taseen tilikauden päättyessä. 

## Perusversion tarjoama toiminnallisuus

Ensimmäisessä vaiheessa toteutetaan versio, joka pyytää käyttäjältä Nordean tilitapahtumista muodostetun CSV-tiedoston (tehty).
Käyttäjälle tarjotaan mahdollisuutta antaa pankkitilin saldo tilikauden alkua edeltävänä päivänä. Tilikartta pidetään
minimissä: tuloslaskelman ainoat tilit ovat Tulot ja Menot ja vastaavasti taseen ainoa tili on Varat. Käyttäjä
pääsee tässä vaiheessa ainoastaan näkemään, paljonko rahaa on tullut ja mennyt. Sovellus tulostaa raportit tietokoneen
näytölle tekstinä (tehty kassavirtalaskelma ja tuloslaskelma).

## Perusversion jälkeen lisättävät toiminnallisuudet

Kun ohjelmasta on saatu toimiva perusversio, laajennetaan toiminnallisuuksia, jotta sovelluksesta olisi jotain hyötyäkin.
Toiminnallisuuksia on tarkoitus lisätä sen verran, mitä aikataulu sallii ja osa listalla olevista toiminnallisuuksista on
pikemminkin optimistisia tulevaisuuden visioita realistisia tavoitteita, joita ehtisi toteuttaa kurssin aikataulun
puitteissa.

 - Ohjataan käyttäjää laatimaan tilikartta, joka palvelee hänen tarkoituksiaan. Käydään tilitapahtumat läpi ja pyydetään
   käyttäjää valitsemaan niille sopivat vastatilit (esim. sähkölasku merkitään asumismenoksi). (lisätty luokittelu
   minimaalisella tilikartalla: Tulot, Menot, Oma tili, Lainat) 
 - Tarjotaan mahdollisuutta pilkkoa lainanhoitoon liittyvät tilitapahtumat korkomenoihin ja lainanlyhennyksiin.(tehty)
 - Tarjotaan mahdollisuus kyselyihin. Voidaan hakea esim. asumismenot halutulta ajalta tai näyttää vuoden ruokamenot
   kuukausittain. (tehty kysely tilitapahtuman nimellä tai osittaisella nimellä)
 - Tarjotaan mahdollisuutta käyttää myös muista pankeista tulostettuja CSV-tiedostoja ja ohjeistetaan käyttäjä
   muokkaamaan tiedosto muotoon, josta sovellus löytää tarvitsemansa tiedot. (ohjeistettu käyttöohjeessa) 
 - Tarjotaan mahdollisuus lisätä tase-eriä, joista voidaan tehdä tulosvaikutteisia tasapoistoja, esim. kodinkoneet ja 
   huonekalut. Näiden tarkoitus on auttaa käyttäjää hahmottamaan, kuinka paljon kuukaudessa pitäisi jäädä säästöön, jotta
   huonekaluja ja kodinkoneita olisi varaa uusia tarpeen mukaan ilman osamaksuja.
 - Tarjotaan mahdollisuus syöttää yksittäisiä käteisostoksia käyttöliittymän kautta.
 - Tarjotaan mahdollisuus lisätä taseeseen useampia pankkitilejä.(lisätty tilien yhdistäminen, joka muodostaa koontitilin)
 - Lisätään tulostuksiin yksinkertaista grafiikkaa, joka helpottaa kokonaisuuden hahmottamista.(ehkä seuraavassa elämässä)
 
## Haaveissa olevat jatkokehitysideat
 
 - Mahdollisuus lisätä taseeseen luottokortti, jonka tapahtumat saadaan syötettyä PDF-tiedostosta.
 - Mahdollisuus lisätä taseeseen sijoituksia ja mahdollisuus päivittää näiden arvoja. Tähän liittyen lisättäisiin taseeseen
   tilit Sijoitusten käyvän arvon muutos ja Piilevä verovelka.
 - Mahdollisuus laskea erilaisia omaa taloutta kuvaavia tunnuslukuja tilikaudelta.

## Toimintaympäristön rajoitteet

Sovellus toimii Linux-käyttöjärjestelmällä varustetuissa koneissa. Sovellus tallennetaan käyttäjän koneelle ja se
käyttää myös käyttäjän koneen tallennustilaa tilitietojen pysyväistallennukseen.
