# Changelog

## Viikko 3

 - Tehty graafiseen käyttöliittymään kaksi ikkunaa, jotka eivät ole vielä yhteydessä ohjelman muihin osiin
 - Tehty service-kerrokseen luokka TKService, jossa seuraavat toiminnot: 
	- funktio, joka lukee tilitapahtumat ja tallettaa tärkeimmät tiedot sanakirjaan
	- funktio, joka tulostaa sanakirjasta yhteenvedon tuloista ja menoista
 - Lisätty neljä testiä, jotka testaavat TKService-luokan funktioiden toimintoja
 
## Viikko 4

 - Tehty graafiseen käyttöliittymään kilke alkusaldon kyselyä varten, ei ole yhteydessä muihin osiin
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
   voi ilmoittaa maksettujen korkojen osuuden
 - Lisätty servicen tallennusfunktioon lainatapahtumien erittely, joka erittelee korot menoihin ja lyhennykset
   lainoihin (tase)
 - Lisätty tallennusfunktiolle testi, joka toistaiseksi vasta tarkistaa, ettei tallennusfunktio kaadu
   (tallennuksen toimintaa on tarkasteltu silmämääräisesti)
 - Parannettu tiedostopolkuja

