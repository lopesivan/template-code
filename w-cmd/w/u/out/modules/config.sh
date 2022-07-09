# modules/config.sh

function ttjava.config.load () {

    b.unset 'ttjava.config'

    _ttjava.config.load_default_config

    return $?
}

function _ttjava.config.load_from_file () {

    local file="$1"

    local number_of_tasks=$(cat $file | jq '.ttjava[] .start' | wc -l)
    let number_of_tasks--
    for i in `seq 0 $number_of_tasks`; do

        local command=$(cat $file |
            jq --raw-output ".ttjava[$i].command")

        local description=$(cat $file |
            jq --raw-output ".ttjava[$i].description")

        b.set "ttjava.config.help_message_$command" "$description"
    done

    local name=$(cat $file | jq --raw-output ".id.name")

    local version=$(cat $file | jq --raw-output ".id.version")

    b.set "ttjava.config.name" "$name"
    b.set "ttjava.config.version" "$version"
    b.set "ttjava.config.author" "`git config --get user.name`"
    b.set "ttjava.config.email"  "`git config --get user.email`"

}

function _ttjava.config.load_default_config () {

    b.set "ttjava.config.help_message" '2'

    local file="$(dirname $(readlink -f $(which ttjava)))/etc/ttjavadoc.json"

    if [ -n "$file" ]; then                   # se variavel nao nula
        if [ -e "$file" ]; then               # se arquivo existe
            _ttjava.config.load_from_file "$file" # carrega arquivo

            return $?
        else
            b.raise FileNotFoundException     # se arquivo nao encontrado
        fi
    else
        b.raise StringIsNullException         # se a variavel e nula
    fi

    return 1
}

# vim: set ts=4 sw=4 tw=78 ft=sh:
