SELECT * FROM temperatura;

-- dohvacanje zadnjeg reda
SELECT * FROM temperatura
ORDER BY id DESC
LIMIT 1;

-- spajanje korisnika i ovlasti
SELECT ime, prezime, naziv FROM korisnik 
INNER JOIN ovlasti ON id_ovlasti = ovlasti.id;


SELECT * FROM korisnik WHERE username = 'kkolar' and password = '12ab';

-- z7 visestruki upit
SELECT ime, prezime, vrijednost, naziv FROM korisnik
INNER JOIN ovlasti ON ovlasti.id = korisnik.id_ovlasti
INNER JOIN korisnikove_temperature ON korisnik.id = korisnikove_temperature.id_korisnika
INNER JOIN temperatura ON korisnikove_temperature.id_temperature = temperatura.id;

SELECT ime, prezime FROM korisnik WHERE naziv = 'Korisnik';