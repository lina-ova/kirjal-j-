 # Kirjaläjä 
Kurssiprojekti Helsingin yliopiston Tietokantasovellus-kurssille

Sovelluksen on tarkoitus olla kirjafoorumi, jossa käyttäjät kirjautua kommentoida kirjoja



Sovelluksen ominaisuuksia ovat:

  Sovelluksessa on kahdenlaisia käyttäjiä: tavallinen käyttäjä ja admin käyttäjä

Tavallinen käyttäjä voi:
  * kirjautua salasanalla ja tunnuksella tai luoda uudet
  * kommentoida kirjan
  * poistaa lisäämänsä komentin
  * tykätä kommenteistä ja kirjoista
  * etsia kirjan kirjoittajan nimen tai kirjan nimen perusteella
  * antaa palautten sovelluksen kehittäjälle
  * filteröidä kirjat genreen ja omien tykkäyksien perusteella
tavallisen käyttäjän oikeuksien lisäksi admin voi:
  * luoda uuden kirjan. Kirjalle on sitten kirjoitettava kirjan nimen, kirjailijan, kuvauksen ja valita genre listasta yhden tai useamman genren ja halutessaan myös linkin kansikuvaan.
  * Jos sopivaa genreä ei löydy listalta - Admin voi lisätä uuden genren. 
  * poistaa kirjoja ja muiden käyttäjien komentteja
  * nähdä muiden antamia palautteita ja poistaa niitä

## Sovelluksen tilanne



Sovelluksen toiminnallisuudet ja ulkoasu ovat tältä erää valmiina
 ## Mahdollisia jatkokehityskohteita

 * käyttäjä voi vastata muiden antantamiin komennteihin
 * käyttäjä voi tehdä haun yhden genren sisällä 
 * leffoille voi tehdä oman samankaltaisen valikon

## käynnistysohje
Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql
Nyt voit käynnistää sovelluksen komennolla

$ flask run