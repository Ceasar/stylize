"============================================================================
"File:        stylize.vim
"Description: Syntax checking plugin for syntastic.vim
"Maintainer:  LCD 47 <lcd047 at gmail dot com>
"License:     This program is free software. It comes without any warranty,
"             to the extent permitted by applicable law. You can redistribute
"             it and/or modify it under the terms of the Do What The Fuck You
"             Want To Public License, Version 2, as published by Sam Hocevar.
"             See http://sam.zoy.org/wtfpl/COPYING for more details.
"
"============================================================================
"
" For details about stylize see: https://github.com/Ceasar/stylize

if exists("g:loaded_syntastic_md_stylize_checker")
    finish
endif
let g:loaded_syntastic_md_stylize_checker=1

function! SyntaxCheckers_md_stylize_IsAvailable()
    return executable('stylize')
endfunction

function! SyntaxCheckers_md_stylize_GetLocList()
    let makeprg = syntastic#makeprg#build({
        \ 'exe': 'stylize',
        \ 'filetype': 'md',
        \ 'subchecker': 'stylize' })

    let errorformat = '%f:%l:%c: %m'

    let loclist = SyntasticMake({
        \ 'makeprg': makeprg,
        \ 'errorformat': errorformat,
        \ 'subtype': 'Style' })

    for n in range(len(loclist))
        let loclist[n]['type'] = loclist[n]['text'] =~? '^W' ? 'W' : 'E'
    endfor

    return loclist
endfunction

call g:SyntasticRegistry.CreateAndRegisterChecker({
    \ 'filetype': 'md',
    \ 'name': 'stylize'})
