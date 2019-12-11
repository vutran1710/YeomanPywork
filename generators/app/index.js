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
        name: 'deps',
        message: 'What kind of libs you want to install?',
        choices: [
          'redis',
          'aioredis',
          'mysql',
          'cassandra',
          'fastapi',
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
      this.templatePath(''),
      this.destinationPath(''),
      { globOptions: { dot: true } },
    )

    // Write to template
    const deps = this.props.deps.reduce((depObj, item) => ({
      ...depObj,
      [item]: true,
    }), {
      redis: false,
      aioredis: false,
      mysql: false,
      cassandra: false,
      fastapi: false,
    })

    this.fs.copyTpl(
      this.templatePath('Pipfile'),
      this.destinationPath('Pipfile'),
      deps,
    )

    this.fs.copyTpl(
      this.templatePath('utils.py'),
      this.destinationPath('utils.py'),
      deps,
    )

    this.fs.copyTpl(
      this.templatePath('config.ini'),
      this.destinationPath('config.ini'),
      deps,
    )

    this.fs.copyTpl(
      this.templatePath('main.py'),
      this.destinationPath('main.py'),
      { project: this.props.project },
    )
  }

  async install() {
    this.spawnCommand('pipenv', ['install', '--dev'])
  }
}
