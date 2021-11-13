FROM pypy:3.7
#ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update
RUN apt-get install -y build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev git python3-pip
RUN python -m pip install pynvim

RUN  apt-get update \
  && apt-get install -y neovim \
  && apt-get install -y curl
RUN wget https://github.com/neovim/neovim/releases/download/v0.5.0/nvim.appimage \
&& chmod u+x nvim.appimage \
&& ./nvim.appimage --appimage-extract \
&& cp ./squashfs-root/usr/bin/nvim /usr/bin/vim \
&& rm -rf nvim.appimage squashfs

WORKDIR /root
RUN curl https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh > installer.sh \
&& sh ./installer.sh ~/.cache/dein \
&& rm installer.sh
RUN  curl -sL install-node.now.sh/lts >install.sh \
&& chmod +x install.sh \
&& ./install.sh --yes \
&& rm install.sh

RUN python -m pip install jedi online-judge-tools

COPY plugins /root/.config/nvim/plugins
COPY init.vim /root/.config/nvim/init.vim
COPY python.snip /root/mysnippet/python.snip
COPY ac /root/ac
#COPY ac /root/ac
# vim plugin install
RUN nvim +"call dein#install()" +qall
# coc extension install 無理やりステータスコード0に
RUN vim -c 'CocInstall -sync coc-json coc-jedi|q' || true

CMD ["bash"]
