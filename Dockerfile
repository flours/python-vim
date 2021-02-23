FROM ubuntu 
RUN apt update
RUN apt install -y vim git

RUN mkdir -p /root/.vim/bundle
COPY .vimrc /root/.vimrc
RUN git clone git://github.com/Shougo/neobundle.vim /root/.vim/bundle/neobundle.vim

# Todo get vimproc

RUN vim -N -u NONE -i NONE -V1 -e -s --cmd "source ~/.vimrc" --cmd NeoBundleInstall! --cmd qall!

CMD ["vim"]

