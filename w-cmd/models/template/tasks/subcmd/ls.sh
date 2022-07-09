# tasks/ls.sh
function btask.ls.run() {
    if [ "$1" == '--help' ]; then
        b.get "template.config.help_message_ls"

        return $( b.get "template.config.help_message" )
    fi

    find $(dirname $(readlink -f $(which template)))/tasks/subcmd \
        -name \*.sh \
        -printf "%f\n" |
    sed 's/\.sh$//'    |
    xargs -n1          |
    sort
}

# vim: set ts=4 sw=4 tw=78 ft=sh:
