if exists('g:loaded_ac_nvim') || !has('nvim')
  finish 
endif
command! Setuser call luaeval("require('ac').set_user()")
command! Setpass call luaeval("require('ac').set_pass()")
command! Setcontest call luaeval("require('ac').set_contest()")

command! -nargs=+ Test call Test(<f-args>)
command! -nargs=+ Submit call Submit(<f-args>)
command! Login call luaeval("require('ac').login()")
command! Alg call luaeval("require('ac').algorithm_picker()")

function! Test(...)
  if a:0==1
    call luaeval("require('ac').test('".a:1."')")
  end
  if a:0==2
    call luaeval("require('ac').test_with_lang('".a:1."','".a:2."')")
  end
endfunction

function! Submit(...)
  if a:0==1
    call luaeval("require('ac').submit('".a:1."')")
  end
  if a:0==2
    call luaeval("require('ac').submit_with_lang('".a:1."','".a:2."')")
  end
endfunction

let g:loaded_ac_nvim=1
