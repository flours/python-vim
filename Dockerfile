FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev git
RUN apt-get install -y python3-pip
RUN pip3 install pynvim

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:neovim-ppa/stable \
  && apt-get update \
  && apt-get install -y neovim \
  && apt-get install -y curl
WORKDIR /root
RUN curl https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh > installer.sh
RUN sh ./installer.sh ~/.cache/dein
COPY init.vim /root/.config/nvim/init.vim
COPY python.snip /root/mysnippet/python.snip
CMD ["bash"]
