# GEDEA

Aplicación web de gestión de estándares abiertos desarrollada en [Django](https://www.djangoproject.com/) para la [OSL](https://osl.ull.es/).

> Esta aplicación web sigue la Política de los Estándares Abiertos aprobada por la ULL


## Requisitos | Requirements

Los siguientes paquetes han sido utilizados en el desarrollo de la aplicación web:

* [Python](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
    * **Versión:** Python 3.5.1+
* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
    * **Versión:** Django 1.8.7
* [Django-Cas](https://bitbucket.org/cpcc/django-cas) - django_cas is a CAS 1.0 and CAS 2.0 authentication backend for Django.
    * **Última revisión:** 1 de abril del 2013.
* [Scrapy-Python](http://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites. 
    * **Versión:** Scrapy 1.1
* [Docker](https://www.docker.com/) - An open platform for distributed applications for developers and sysadmins.
    * **Versión:** 
```
Client:
 Version:      1.11.1
 API version:  1.23
 Go version:   go1.5.4
 Git commit:   5604cbe
 Built:        Tue Apr 26 23:43:49 2016
 OS/Arch:      linux/amd64

Server:
 Version:      1.11.1
 API version:  1.23
 Go version:   go1.5.4
 Git commit:   5604cbe
 Built:        Tue Apr 26 23:43:49 2016
 OS/Arch:      linux/amd64
```
* [rt-Python](https://pypi.python.org/pypi/rt) - Python interface to Request Tracker API.
    * **Versión:** rt 1.0.8
* [eclipse](https://eclipse.org/) - Eclipse IDE for Java Developers.
    * **Versión:** Mars.2 Release (4.5.2)
* [eclipse-pydev](http://www.pydev.org/) - PyDev is a Python IDE for Eclipse, which may be used in Python, Jython and IronPython development.
    * **Versión:** PyDev 4.5.5





## Desarrollo | Development
Para que el desarrollo de **gedea** sea más sencillo en una máquina nueva procedemos a la realización del siguiente  `script.sh` con el que será más sencillo la instalación de sus componentes: 

```sh
$ sudo apt-get update        

# Kit de Desarrollo de Java
$ sudo apt-get install default-jdk      
$ java -version 

# Python
$ sudo apt-get install python3-dev      

# Pip
$ sudo apt-get -y install python-pip    

# Scrapy-python
$ sudo pip install scrapy   

# rt-1.0.8
$ wget https://pypi.python.org/packages/00/53/074d1f3af6350491da6712674428bb2441839d34e2b802181a522af3849b/rt-1.0.8.tar.gz
$ tar -xz rt-1.0.8.tar.gz
$ cd rt-1.0.8
$ pip install -r requirements.txt

# Django
$ sudo pip install django
```




## Uso | Usage
Ejecución de nuestra aplicación:
```sh
$ python3 manage.py runserver
```

Actualización de **dataULL.json**:
```sh
$ scrapy runspider -s DEPTH_LIMIT=2 crawl.py -o dataULL.json
```







## Sitio oficial | Official site

Repositorio Git:  [github.com/tic-ull/gedea](https://github.com/tic-ull/gedea)

## Licencia | License
GNU General Public License v3.0

