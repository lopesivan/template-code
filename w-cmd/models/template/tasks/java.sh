# tasks/java.sh
function btask.java.run() {
    if [ "$1" == '--help' ]; then
        b.get "template.config.help_message_java"

        return $( b.get "template.config.help_message" )
    else
        b.task.run "$@"
    fi

}

# vim: set ts=4 sw=4 tw=78 ft=sh:
