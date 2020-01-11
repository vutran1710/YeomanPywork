<p align="center">
  <h1>Pywork</h1><br>
  <i>python app yeoman generator</i><br>
  <a href="https://www.npmjs.com/package/yo">Yeoman</a> |
  <a href="https://www.npmjs.com/package/generator-pywork">Npm Pywork</a> |
  <a href="https://github.com/vutran1710/Pywork">Home</a>
  <br><br>
  <img align="center" width="170" height="170" src="https://raw.githubusercontent.com/vutran1710/YeomanPywork/master/img/pywork.png">
</p>

<br>

`PyWork` is a [Yeoman](http://yeoman.io) generator for a basic python-worker project that makes use of
[Pipenv](https://pipenv.kennethreitz.org/en/latest/), [Logzero](https://logzero.readthedocs.io/en/latest/) and
[Pydantic](https://pydantic-docs.helpmanual.io/).

It includes a bunch of helpful dev-dependencies, being:

- jedi
- flake8
- pylint
- yapf
- pytest

...and few boilerplates for working with different databases/message broker using python clients like

- Redis
- AioRedis
- RabbitMQ
- Cassandra
- MySQL
- PostgreSQL

It supports framework-based application templates for frameworks like:
- [FastApi](https://fastapi.tiangolo.com/)

and more to come...

Some extra useful stuffs provided are:
- Docker:
  + `Dockerfile`
  + `.dockerignore`



## Get set

### Have `Yeoman` installed globally.

``` shell
$ npm install -g yo
```

If you haven't used `Yeoman` before, take a look at the [Yeoman's Official Website](http://yeoman.io) for details.

### Prepare project with Yeoman

- Install `generator-pywork`

``` shell
$ npm install -g generator-pywork
```

- Init a project, w/o `git`

``` shell
$ mkdir my-project && cd my-project
$ yo pywork
```

- Answer setup questions
  + **Project name** :: which is required
  + **Dependencies** :: some database clients you may wanna add, depending on your needs

With each selected database-client or third-party libraries, some extra application config variables may be added to
`config.ini`. So make sure to fix the `config.ini` after having finished installing all dependencies with `Pipenv`.

Formatting config can be changed by editting `setup.cfg`

### Start Coding

If everything else went well, you can start coding your project.
