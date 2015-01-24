# MDM Webapp
Questo repository contiene il codice per lo sviluppo e il deployment del sito web di MDM S.r.l.

## Sviluppo: Vagrant
Per avviare la macchina virtuale contenente l'ambiente di runtime è sufficiente dare il comando `vagrant up`. Per ulteriori informazioni sull'utilizzo di Vagrant si faccia riferimento alla [documentazione ufficiale](https://www.vagrantup.com/).

## Deploy: Docker
Viene "esposto" un volume nel quale sono presenti due elementi:

 * gli asset ed i file statici da servire (cartella `static`);
 * il socket uWSGI per la comunicazione con la webapp. Questo ha nome: _app.sock_

Il volume è in posizione `/export`.

### Opzioni per l'avvio
...aka `docker run [OPTS]`

  * `-v /somepath:/export` (bind mount del volume sopra descritto)
  * `-h my.name.com` (FQDN)
  * `-e STATIC_URL=http://where_are_the_assets.com`

