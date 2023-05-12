# Talouskatsaus

Ohjelman tarkoitus on koota yhteenveto käyttäjän antamasta tiliotteesta. Ohjelmaa voi käyttää myös tietojen yhdistelyyn useammalta
eri tililtä. Ohjelma on tarkoitettu yhdelle käyttäjälle, mutta toki siihen voi tallentaa kahdenkin ihmisen tilitiedot, jos halutaan
saada kokonaiskuva perheen taloudesta.Ohjelma pystyy käsittelemään Nordean ja S-Pankin tiliotteita.

Ohjelmaa voi kokeilla päähakemiston tiedostoilla Nordea.csv ja S-Pankki.csv.

Disclaimer: Käyttöohjetta ei ole päivitetty täysin edellisen releasen jäljiltä vastaamaan kaikkia toimintoja, mutta se kannattaa silti lukea.

[Viimeisin release](https://github.com/rpessi/ot-harjoitustyo/releases/tag/loppupalautus)

## Python-versio

Ohjelman toiminta on testattu Python-versiolla 3.8. Erityisesti tätä vanhempien Python-versioiden kanssa saattaa
esiintyä ongelmia. 

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Työajan seuranta](./dokumentaatio/tuntikirjanpito.md)

## Ohjelman asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Sovelluksen voi käynnistää komennolla:

```bash
poetry run invoke start
```

Valitettavasti tämän käynnistystavan kanssa esiintyy jostain syystä tulostuksessa ongelmia. Taulukot tulostuvat oikein, kun käynnistät
ohjelman seuraavilla komennoilla:

```bash
poetry shell
```

```bash
poetry run python3 src/index.py
```

Kaikki ylläolevat komennot suoritetaan siinä hakemistossa, mihin ohjelma on ladattu. 


## Komentorivitoiminnot

### Ohjelman käynnistäminen

Ohjelman pystyy käynnistämään komennolla:

```bash
poetry run invoke start
```

### Ohjelman automaattinen testaus

Automaattiset testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon

### Pylint

Koodin laaduntarkkailijana ja tyylipoliisina toimii Pylint. Tiedoston [.pylintrc](./.pylintrc) määrittelemät 
tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
