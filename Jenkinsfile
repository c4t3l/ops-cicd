node('kitchen-salt') {
  stage('setup'){
  deleteDir()
  }

stage('scm'){
  checkout([$class: 'GitSCM',
  branches: [[name: '*/dev']],
  doGenerateSubmoduleConfigurations: false,
  extensions: [[$class: 'CleanBeforeCheckout']],
  submoduleCfg: [],
  userRemoteConfigs: [[credentialsId: 'ops_deploy_ssh', url: '"git@github.com:c4t3l/ops-cicd.git"']]])
  }

stage('build') {
  // Run kitchen tests
  sh './util.sh -k'
  }

stage('merge to test') {
  sshagent(['ops_deploy_ssh']) {
    sh 'git fetch --all'
    sh 'git checkout --track origin/dev'
    sh 'git checkout --track origin/test'
    sh 'git branch --set-upstream-to origin/test'
    //sh 'git show-ref'

    sh 'git merge dev'

    // git configs
    sh 'git config user.email ops_deploy@eogresources.com'
    sh 'git config user.name ops_deploy'
    sh 'git config push.default upstream'

    //Merge and push to upstream test branch
    sh 'git add .'
    sh 'git commit --amend -m "Merged via ops_deploy." --author="ops_deploy <ops_deploy@eogresources.com>"'
    sh 'git remote -v'
    sh 'git push origin	test --force'
    }
}
stage('create PR') {
  // Generate pull request to master branch from here
  sh './util.sh -m'
  }
}

