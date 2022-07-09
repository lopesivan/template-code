# tasks/beans.sh
function btask.beans.run() {
    if [ "$1" == '--help' ]; then
        b.get "template.config.help_message_beans"

        return $( b.get "template.config.help_message" )
    fi


}

# vim: set ts=4 sw=4 tw=78 ft=sh:
