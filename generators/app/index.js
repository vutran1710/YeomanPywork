/*
 * Generator index
 */
const Generator = require('yeoman-generator')
const chalk = require('chalk')
const yosay = require('yosay')

module.exports = class extends Generator {
  constructor(args, opts) {
    super(args, opts)
  }

  prompting() {
    // Have Yeoman greet the user.
    const greet = 'Scaffolding with Taste, ' + chalk.red('A Bare-bone Python Project')
    this.log(yosay(greet))

    let prompts = [
      {
        type: 'input',
        name: 'project',
        message: 'What is your project name?',
        default: '',
        store: true
      },
      {
        type: 'input',
        name: 'git_url',
        message: 'Optionally give us the git remote url of your repo:',
        default: '',
        store: true
      },
      {
        type: 'checkbox',
        name: 'connections',
        message: 'What kind of connection libs you want to install?',
        choices: [
          'rabbitmq',
          'redis',
          'aioredis',
          'mysql',
          'cassandra',
          'fastapi',
        ],
        default: [],
        store: true
      },
      {
        type: 'checkbox',
        name: 'framework',
        message: 'What kind of frameworks you want to install?',
        choices: [
          'fastapi',
          // 'falcon',
          // 'starlette',
          // 'aiohttp',
        ],
        default: [],
        store: true
      },
    ]

    return this.prompt(prompts).then(props => {
      this.log(props)
      this.props = props
      // To access props later use this.props.someOption
    })
  }

  writing() {
    // Copy static files recursively
    this.fs.copy(
      this.templatePath('app'),
      this.destinationPath('app'),
      { globOptions: { dot: true } },
    )

    this.fs.copy(
      this.templatePath('tests'),
      this.destinationPath('tests'),
      { globOptions: { dot: true } },
    )

    // Write to template
    const connections = this.props.connections.reduce((depObj, item) => ({
      ...depObj,
      [item]: true,
    }), {
      rabbitmq: false,
      redis: false,
      aioredis: false,
      mysql: false,
      cassandra: false,
    })

    this.fs.copyTpl(
      this.templatePath('Pipfile'),
      this.destinationPath('Pipfile'),
      connections,
    )

    this.fs.copyTpl(
      this.templatePath('utils.py'),
      this.destinationPath('utils.py'),
      connections,
    )

    this.fs.copyTpl(
      this.templatePath('config.ini'),
      this.destinationPath('config.ini'),
      connections,
    )

    this.fs.copyTpl(
      this.templatePath('main.py'),
      this.destinationPath('main.py'),
      { project: this.props.project },
    )

    // Conditional modules...
    if (this.props.connections.length > 0) {
      this.fs.copy(
        this.templatePath('conn/__init__.py'),
        this.destinationPath('conn/__init__.py'),
      )
    }

    if (connections.redis || connections.aioredis) {
      this.fs.copyTpl(
        this.templatePath('conn/redis.py'),
        this.destinationPath('conn/redis.py'),
        connections,
      )
    }
  }

  async install() {
    this.spawnCommand('pipenv', ['install', '--dev'])
  }
}
