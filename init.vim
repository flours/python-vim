set number
set tabstop=2
set expandtab
set smartindent
set smartindent
set list listchars=tab:\▸\-
set cursorline
set cursorcolumn
set completeopt=menuone
set shiftwidth=2
" 検索系
" 検索文字列が小文字の場合は大文字小文字を区別なく検索する
set ignorecase
" 検索文字列に大文字が含まれている場合は区別して検索する
set smartcase
" 検索文字列入力時に順次対象文字列にヒットさせる
set incsearch
" 検索時に最後まで行ったら最初に戻る
set wrapscan
" 検索語をハイライト表示
set hlsearch
" ESC連打でハイライト解除
nmap <Esc><Esc> :nohlsearch<CR><Esc>



set showtabline=2 
"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

let s:plugin = '~/.config/nvim/plugins/config/dein.toml'



" Required:
set runtimepath+=/root/.cache/dein/repos/github.com/Shougo/dein.vim
" Let dein manage dein


if dein#load_state('~/.cache/dein')
  call dein#begin('~/.cache/dein')
  " dein.tomlを起動時ロードの設定ファイルとして読み込む
  call dein#load_toml(s:plugin, {'lazy': 0})
  call dein#end()
  call dein#save_state()
endif

if dein#check_install()
  call dein#install()
endif



" Required:
filetype plugin indent on
syntax enable

"End dein Scripts-------------------------

" Plugin key-mappings.
" Note: It must be "imap" and "smap".  It uses <Plug> mappings.
imap <C-k>     <Plug>(neosnippet_expand_or_jump)
smap <C-k>     <Plug>(neosnippet_expand_or_jump)
xmap <C-k>     <Plug>(neosnippet_expand_target)

" SuperTab like snippets behavior.
" Note: It must be "imap" and "smap".  It uses <Plug> mappings.
"imap <expr><TAB>
" \ pumvisible() ? "\<C-n>" :
" \ neosnippet#expandable_or_jumpable() ?
" \    "\<Plug>(neosnippet_expand_or_jump)" : "\<TAB>"
smap <expr><TAB> neosnippet#expandable_or_jumpable() ?
\ "\<Plug>(neosnippet_expand_or_jump)" : "\<TAB>"

" For conceal markers.
if has('conceal')
  set conceallevel=2 concealcursor=niv
endif

let s:my_snippet = '~/mysnippet'
let g:neosnippet#snippets_directory = s:my_snippet
autocmd InsertLeave * set nopaste
imap <C-c> <Esc>
set cursorline
highlight CursorLine ctermbg=5
set belloff=all
set mouse=a

let aa=system("python /root/ASCII-Art-Splash-Screen/ascii.py 2>/dev/null")
let words = split(aa,"\n")
let g:startify_custom_header = words
