/*
 * Generator index
 */
const Generator = require('yeoman-generator')

module.exports = class extends Generator {
  constructor(args, opts) {
    super(args, opts)
    this.argument('project_name', { type: String, required: true })
  }

  prompting() {
    // Have Yeoman greet the user.
    const greet = 'Scaffolding with Taste, ' + chalk.red('A Bare-bone Python Project')
    this.log(yosay(greet))

    let prompts = [
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
      self.templatePath('Pipfile'),
      self.destinationPath('Pipfile'),
    )

    this.fs.copy(
      self.templatePath('utils.py'),
      self.destinationPath('utils.py'),
    )

    this.fs.copy(
      self.templatePath('config.ini'),
      self.destinationPath('config.ini'),
    )
  }

  install() {
    this.spawnCommand('pipenv', ['install', '--dev'])
  }
}
