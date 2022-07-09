_template()
{
    COMPREPLY=()
    local word="${COMP_WORDS[COMP_CWORD]}"

    if [ "$COMP_CWORD" -eq 1 ]; then
        COMPREPLY=( $(compgen -W "$(template commands)" -- "$word") )
    # else
    #     local words=("${COMP_WORDS[@]}")

    #     case x${words[1]} in
    #         xnew)
    #             unset words[0]
    #             unset words[$COMP_CWORD]
    #             local completions=$(template new -l "${words[@]}" )
    #             COMPREPLY=( $(compgen -W "$completions" -- "$word") )
    #         ;;
    #     esac

    fi
}
complete -F _template template
