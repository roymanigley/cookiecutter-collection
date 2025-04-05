#!/bin/bash

git clone https://github.com/Yggdroot/LeaderF [[ cookiecutter.vim_dir ]]/pack/plugins/start/LeaderF
git clone https://github.com/liuchengxu/vim-which-key.git [[ cookiecutter.vim_dir ]]/pack/plugins/start/vim-which-key
git clone https://github.com/mg979/vim-visual-multi.git [[ cookiecutter.vim_dir ]]/pack/plugins/start/vim-visual-multi
git clone https://tpope.io/vim/commentary.git [[ cookiecutter.vim_dir ]]/pack/plugins/start/commentary
git clone https://github.com/davidhalter/jedi-vim [[ cookiecutter.vim_dir ]]/pack/plugins/start/jedi-vim

cp .vimrc [[ cookiecutter.vim_dir ]]

/bin/vim -u [[ cookiecutter.vim_dir ]]/.vimrc -c 'LeaderfInstallCExtension' -c 'qa'
