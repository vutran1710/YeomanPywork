/*
 * Generator index
 */
const Generator = require('yeoman-generator')

module.exports = class extends Generator {
  constructor(args, opts) {
    super(args, opts)
    this.argument("project_name", { type: String, required: false })
  }

  prompting() {
    // Have Yeoman greet the user.
    this.log(
      yosay(
        "Mess with the best, " + chalk.red("Django likes REST...") + " Yeah..."
      )
    )

    let prompts = [
      {
        type: "confirm",
        name: "prod_branch",
        message:
          "You want a create-react-app frontend that compiles to a separate prod branch?",
        default: false,
        store: true
      },
      {
        type: "input",
        name: "git_url",
        message: "Optionally give us the git remote url of your repo:",
        default: "",
        store: true
      },
      {
        type: "input",
        name: "heroku_url",
        message:
          "...and if you want to deploy to Heroku, the Heroku git url too:",
        default: "",
        store: true
      }
    ]

    // if project_name wasn't passed in as an argument
    if (!this.options.project_name) {
      prompts = [
        {
          type: "input",
          name: "project_name",
          message: "What is the name of your project?",
          default: this.appname // Default to current folder name
          //store   : true // ? http://yeoman.io/authoring/user-interactions.html
        },
        ...prompts
      ]
    }

    return this.prompt(prompts).then(props => {
      this.props = props
      // To access props later use this.props.someOption
      if (!this.props.project_name) {
        this.props.project_name = this.options.project_name
      }
    })
  }

  writing() {
    // django
    // - first without the mysite module
    this.fs.copyTpl(
      this.templatePath("django/mysite/!(mysite){/**/*,*}"),
      //this.destinationPath('/whydoineedthis/'),
      this.destinationPath("./whydoineedthis/"),
      this.props
    )
    this.fs.copyTpl(
      this.templatePath("django/mysite/mysite/{/**/*,*}"),
      this.destinationPath(this.props.project_name + "/whydoineedthis/"),
      this.props
    )

    // static
    if (!this.props.prod_branch) {
      this.fs.copyTpl(
        this.templatePath("static/{/**/*,*}"),
        this.destinationPath(
          this.props.project_name + "/static/whydoineedthis/"
        ),
        this.props
      )
    }

    // projectfiles
    this.fs.copyTpl(
      this.templatePath("projectfiles/{*,.*}"),
      this.destinationPath("./"),
      this.props
    )
  }

  install() {
    //this.installDependencies()
  }
}
