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
tavallisen käyttäjän oikeuksien lisäksi admin voi:
  * luoda uuden kirjan. Kirjalle on sitten kirjoitettava kirjan nimen, kirjailijan, kuvauksen ja valita genre listasta yhden tai useamman genren ja halutessaan myös linkin kansikuvaan.
  * Jos sopivaa genreä ei löydy listalta - Admin voi lisätä uuden genren. 
  * poistaa kirjoja ja muiden käyttäjien komentteja

## Sovelluksen tilanne
Sovellus on testattavissa täällä

Sivustolle tullessaan ylävalikosta löytyy linkit pääsivulle, uuden käyttäjätunnuksen tekemiseen ja sisäänkirjautumiseen. Sisäänkirjautumisen jälkeen ylävalikosta löytyy linkki uloskirjautumiseen, palautteen antamiseen ja admin käyttäjillä linkki uuden kirjan lisäämiseen

Pääsivulla löytyy lista lisäämistä kirjoista. Kullakn kirjalla kijan ja kirjailija nimi, nappi kirjan tykkäykseen ja kansikuva, joka toimii linkkinä kirjan omalle sivulle. 
Kansikuva on joko admin käytäjän lisäämä tai default kuva
Admin käyttäjillä on myös nappi kirjan poistamiseen. 

Kirjan omalla sivulla löytyy kansikuva, kirjan tarkemmat tiedot, kuten nimi, kirjailija, genret ja tähdet, joka on keskiarvo käyttäjien antamistä tehdistä. 
Sivulla näkyy myös muiden käyttäjien antamat arvostelut. 
Käyttäjä voi poistaa itse antamat arvostelut. Admin käyttäjä voi poistaa minkä tahansa arvostelun.
kirjautuneille käyttäjile näkyy kirjan arvostelunanto teksikenttä ja tähti valikko. Käyttäjä voi antaa kirjalle 1-5 tähtiä. 


Sovelluksen toiminnallisuudet ja ulkoasu ovat tältä erää valmiina. Mahdollisia jatkokehitysideoita ovat