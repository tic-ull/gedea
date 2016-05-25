# GEDEA

Aplicación web de gestión de estándares abiertos desarrollada en [Django](https://www.djangoproject.com/) para la [OSL](https://osl.ull.es/).

> Esta aplicación web sigue la Política de los Estándares Abiertos aprobada por la ULL


## Requísitos | Requirements

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


## Instalación | Installation







## Desarrollo | Development

Necesitamos el **Kit de Desarrollo de Java** instalado globalmente para instalar nuestro entorno de desarrollo que será **eclipse + pydev**:
```sh
$ sudo apt-get install default-jdk
$ java -version
```

Necesitamos **Python**:
```sh
sudo apt-get install python3-dev
```

Necesitamos el **Scrapy-Python** para la actualización de nuestro dataULL.json:
```sh
$ pip install scrapy
```

## Uso | Usage
Ejecución de nuestra aplicación:
```sh
$ python3 manage.py runserver
```

Actualización de **dataULL.json**:
```sh
$ scrapy runspider -s DEPTH_LIMIT=2 crawl.py `-o dataULL.json
```







## Sitio oficial | Official site

Repositorio Git:  [github.com/tic-ull/gedea](https://github.com/tic-ull/gedea)

## Licencia | License
GNU General Public License v3.0

