# Changelog

## Viikko 3

 - Tehty graafiseen käyttöliittymään kaksi ikkunaa, jotka eivät ole vielä yhteydessä ohjelman muihin osiin
 - Tehty service-kerrokseen luokka TKService, jossa seuraavat toiminnot: 
	- funktio, joka lukee tilitapahtumat ja tallettaa tärkeimmät tiedot sanakirjaan
	- funktio, joka tulostaa sanakirjasta yhteenvedon tuloista ja menoista
 - Lisätty neljä testiä, jotka testaavat TKService-luokan funktioiden toimintoja
 
## Viikko 4

 - Tehty graafiseen käyttöliittymään kilke alkusaldon kyselyä varten, joka ei ole yhteydessä muihin osiin
 - Lisätty kysely tilitapahtumien luokittelua varten ja siirretty tämä servicestä ui-kansioon
 - Kytketty tekstikäyttöliittymä mainiin
 - Lisätty serviceen funktio tilitietojen ja luokittelujen tallennusta varten (ei toimi vielä kaikilta osin
   toivotulla tavalla
 - Havaittu, että ohjelma kaatuu, jos käyttäjä pyytää yhteenvetoa, ennen kuin tilitietoja on annettu, tämä
   on vielä korjaamatta

## Viikko 5

 - Tehty alkuvalikkoon tarkistus, jotta ohjelma ei kaadu valittaessa yhteenvetoa tilanteessa, jossa käyttäjä ei
   ole antanut vielä tilitietoja
 - Lisätty tilitapahtumien luokittelukyselyyn lainojen kohdalle lainatapahtuman pilkkominen, jossa käyttäjä
   voi ilmoittaa tilikaudella maksettujen korkojen määrän
 - Lisätty servicen tallennusfunktioon lainatapahtumien erittely, joka erittelee korot menoihin ja lyhennykset
   lainoihin (tase)
 - Lisätty tallennusfunktiolle testi, joka toistaiseksi vasta tarkistaa, ettei tallennusfunktio kaadu
   (tallennuksen toimintaa on tarkasteltu silmämääräisesti)
 - Parannettu tiedostopolkuja
 - Lisätty serviceen funktio, joka tulostaa tuloslaskelman ja tehty tälle testit.
 - Lisätty testejä servicen funktiolle, joka tulostaa kassavirtalaskelman.
 
## Viikko 6

 - Lisätty annettujen tilitietojen tallennus JSON-muodossa
 - Lisätty mahdollisuus etsiä tallennetuista tilitiedoista tapahtumia tilin nimen ja tapahtuman (osittaisen) nimen
   perusteella.
 - Lisätty mahdollisuus yhdistää tallennetut tilit. Tämän jälkeen tili Yhdistetty näkyy tapahtumahaussa muiden tilien tapaan
   ja siltä voi hakea tapahtumia kuiten muiltakin tileiltä.
 - Lisätty testit toiminnolle, joka yhdistää tilien tiedot
 - Lisätty tapahtumahaku ja tilien yhdistäminen käyttöliittymän päävalikkoon. Tehty kyselyfunktio tapahtumahakuja varten.
 - Paranneltu edelleen tallennusten tiedostopolkuja.
 - Lisätty tapahtumahakuun tallennettujen tilien luettelo valikkona, jotta käyttäjä ei pääse väärällä haulla kaatamaan ohjelmaa.
 
## Viikot 7-8

 - Muokattu käyttöliittymää siten, että se tarjoaa toimintavalikossa ainoastaan niitä vaihtoehtoja, jotka käyttäjä pystyy
   aidosti valitsemaan. Kun ohjelma käynnistetään ensimmäistä kertaa eikä tallennettuja tilejä vielä ole, valikossa 
   näkyvät vain vaihtoehdot tilien tallentamiseen ja lopettamiseen. 
 - Lisätty funktiot, jotka laskevat raportteja JSON-tallennetuista tiedoista.
 - Lisätty testit raportinlaskentafunktioille.
 - Lisätty toiminto, joka mahdollistaa S-Pankin tiliotteen käyttämisen.
 - Lisätty testi funktiolle, joka muuntaa S-Pankin tiliotteen Nordean tiliotteen kaltaiseksi
 - Poistettu toiminto, joka tarjosi mahdollisuuden tulostuksiin tilapäistallennetun tiedon pohjalta
 - Poistettu testit, jotka testasivat tilapäistallennetun tiedon pohjalta tehtyjä tulostuksia
 - Lisätty toiminto, joka mahdollistaa raporttien tulostamisen pysyväisesti tallennetun tiedon pohjalta
 - Otettu käyttöön Rich-kirjasto, jonka myötä on saatu paranneltua raporttien tulostusta ja parannettu syötteiden pyytämistä
   käyttäjältä
 - Poistettu tapahtumahausta tilivalikko ja korvattu valinta Richin Promptilla
 - Lisätty funktiot raporttitietojen muotoilulle ja tulostukselle, otettu raporttien tulostuksessa käyttöön Rich Console
   ja Rich Table
 - Lisätty tulostusfunktio, joka tulostaa käyttäjälle kuittauksen onnistuneesta tapahtumasta tietyissä tilanteissa tai
   kertoo, että joku vaihe on saatu valmiiksi.
 - Päivitetty käyttöohje vastaamaan ohjelman todellista toiminnallisuutta. Päivitetty käyttöohjeessa olevat kuvat
   vastaamaan sitä, miltä ohjelman lopullinen versio näyttää. Lisätty kuvat raporttien tulosteista ja kuvailtu lyhyesti,
   miten niissä näkyviä tapahtumia tulkitaan. Lisätty myös kuvia ohjelman käytöstä eri tilanteissa ja ohjeistettu
   vaihtoehtoinen tapa ohjelman käynnistämiseen, joka eliminoi ongelmat tulostuksissa, joita ilmenee, kun ohjelma
   käynnistetään Invoken kautta.
