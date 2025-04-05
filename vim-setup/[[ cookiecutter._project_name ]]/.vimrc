" PROPERTIES
set packpath^=[[ cookiecutter.vim_dir ]]
let mapleader = " "
set encoding=UTF-8
set nocompatible
" allow recursive file search from current directory
set path+=./**
" display all matching files when we tab complete
set wildmenu

syntax on
filetype plugin on
set nu
set rnu
set splitbelow

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab

" plugin config WhichKey
let g:which_key_map = {}
let g:which_key_timeout = 10
" plugin config vimwiki
let g:vimwiki_list = [{'path': '~/vimwiki/',
                      \ 'syntax': 'markdown', 'ext': 'md'}]
" KEY BINDINGS
" save on CTRL s (for normal and insert mode)
nnoremap <C-s> :w<CR>
inoremap <C-s> <ESC>:w<CR>a
" theme for gruvbox
set background=dark
" close all on CTRL q (for normal and insert mode)
nnoremap <C-q> :qa<CR>
inoremap <C-q> <ESC>:qa<CR>
" close selected frame on CTRL d (for normal and insert mode)
nnoremap <C-d> :q<CR>
inoremap <C-d> <ESC>:q<CR>

" toggle nerd tree CTRL e
nnoremap <C-e> :NERDTreeToggle<CR>

" show terminal CTRL t
nnoremap <C-t> :terminal<CR>

" trigger WhichKey
nnoremap <silent> <leader> :WhichKey '<Space>'<CR>

" SNIPPETS
" nnoremap ,html :-1read /home/royman/.vim/.skeleton.html<CR>3jwf>a

autocmd vimenter * ++nested colorscheme gruvbox

