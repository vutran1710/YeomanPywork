# generator-pywork
`PyWork` is a [Yeoman](http://yeoman.io) generator for a basic python-worker project that basically makes use of
[Pipenv](), [Logzero]() and [Pydantic](). It also includes a bunch of helpful dev-dependencies, being `jedi`, `flake8`,
`pylint`, `yapf` and certainly `pytest`.


## Get set

### Have `Yeoman` installed globally.

``` shell
$ npm install -g yo
```

If you haven't used `Yeoman` before, take a look at the [Yeoman's Official Website](http://yeoman.io) for details.

### Prepare project with Yeoman

1) Init a project, w/o `git`

``` shell
$ mkdir my-project && cd my-project
$ yo pywork
```

2) Answer setup questions
+ **Project name** :: which is required
+ **Dependencies** :: some database clients you may wanna add, depending on your needs

With each selected database-client or third-party libraries, some extra application config variables may be added to
`config.ini`. So make sure to fix the `config.ini` after having finished installing all dependencies with `Pipenv`.

Formatting config can be changed by editting `setup.cfg`

### Start Coding

If everything else went well, you can start coding your project.
