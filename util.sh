#!/usr/bin/env bash
# This script is used to run tests and generate PRs

set -x

pull_request() {
# Generate PR from test to master
# Eventually this will take input args and will replace kitchen.sh
    curl --request POST \
    --url https://git.eogresources.com/api/v3/repos/ops-salt-formulas/ops-dummy/pulls \
    --user ops_deploy:9c9ad53543bb0741d197df3fc30b83c1a7bbf2fc \
    --header 'content-type: application/json' \
    --data \
    '{
    "title": "Jenkins API PR",
    "body": "Build has passed tests.  Please review and merge.",
    "head": "test",
    "base": "master"
    }'
}

run_kitchen() {
    source ~/.bash_profile
    kitchen test -d
}

gen_help() {
    output="Usage: $(basename utils/ops-reposet/reposet/reposet.sh) [OPTION]\n"
    output+="-h\n\tDisplay this help and exit\n"
    output+="-k\n\tRun kitchen tests\n"
    output+="-m\n\tGenerate Pull Request to Github Enterprise\n"
    echo -ne "${output}"
    exit 22
}

main() {
    while getopts ":mkh" opt; do
    echo "opt is ${opt}"
    case $opt in
        m)
            pull_request;;
        k)
            run_kitchen;;
        h)
            gen_help;;
        \?)
            pull_request;;
    esac
    done
    #gen_help
}

main "$@"

