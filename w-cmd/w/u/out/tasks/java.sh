# tasks/java.sh
function btask.java.run() {
    if [ "$1" == '--help' ]; then
        b.get "ttjava.config.help_message_java"

        return $( b.get "ttjava.config.help_message" )
    else
        [ $0 ] && {
            b.task.run ls
        } || {
            b.task.run "$@"
        }
    fi

}

# vim: set ts=4 sw=4 tw=78 ft=sh:
