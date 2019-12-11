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
        name: 'project_name',
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
          {
            name: 'Redis',
            value: 'redis',
          },
          {
            name: 'Asynchronous Redis',
            value: 'aioredis',
          },
          {
            name: 'MySQL',
            value: 'pymysql',
          },
          {
            name: 'Cassandra',
            value: 'cassandra_driver',
          },
          {
            name: 'FastAPI',
            value: 'fastapi'
          },
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
    // Write to template
    this.fs.copy(
      this.templatePath('Pipfile'),
      this.destinationPath('Pipfile'),
      this.props,
    )

    this.fs.copy(
      this.templatePath('utils.py'),
      this.destinationPath('utils.py'),
      this.props,
    )

    this.fs.copy(
      this.templatePath('config.ini'),
      this.destinationPath('config.ini'),
      this.props,
    )
  }

  install() {
    this.spawnCommand('pipenv', ['install', '--dev'])
  }
}
