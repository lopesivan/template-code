_ttjava()
{
    COMPREPLY=()
    local word="${COMP_WORDS[COMP_CWORD]}"

    if [ "$COMP_CWORD" -eq 1 ]; then
        COMPREPLY=( $(compgen -W "$(ttjava commands)" -- "$word") )
    # else
    #     local words=("${COMP_WORDS[@]}")

    #     case x${words[1]} in
    #         xnew)
    #             unset words[0]
    #             unset words[$COMP_CWORD]
    #             local completions=$(ttjava new -l "${words[@]}" )
    #             COMPREPLY=( $(compgen -W "$completions" -- "$word") )
    #         ;;
    #     esac

    fi
}
complete -F _ttjava ttjava
