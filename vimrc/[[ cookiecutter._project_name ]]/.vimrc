" PROPERTIES
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

" pluginless nerdtree -  set explore properties
let g:netrw_winsize=30	    " define winsize
let g:netrw_banner=0        " disable annoying banner
let g:netrw_browse_split=4  " open in prior window
let g:netrw_altv=1          " open splits to the right
let g:netrw_liststyle=3     " tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

" KEY BINDINGS
" save on CTRL s (for normal and insert mode)
nnoremap <C-s> :w<CR>
inoremap <C-s> <ESC>:w<CR>a

" close all on CTRL q (for normal and insert mode)
nnoremap <C-q> :qa<CR>
inoremap <C-q> <ESC>:qa<CR>
" close selected frame on CTRL d (for normal and insert mode)
nnoremap <C-d> :q<CR>
inoremap <C-d> <ESC>:q<CR>

" toggle nerd tree CTRL e (plugin required)
" nnoremap <C-e> :NERDTreeToggle<CR>
nnoremap <C-e> :Vexplore<CR>

" show terminal CTRL t
nnoremap <C-t> :terminal<CR>

" SNIPPETS
" nnoremap ,html :-1read /home/royman/.vim/.skeleton.html<CR>3jwf>a


