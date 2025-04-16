FROM humble:dev

ARG VERSION=0.0.1


RUN echo "image dev version: ${VERSION}">/etc/docker_image_dev_version

ENV DEBIAN_FRONTEND=noninteractive

# dev: packages that move to dev image
RUN apt-get update \
   && apt-get -y install --no-install-recommends \
    build-essential \
    python3-rosdep \
    python3-bloom \
    fakeroot \
    debhelper \
    dh-python \
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*

# runtime: packages that move to runtime image
RUN apt-get update \
   && apt-get -y install --no-install-recommends \
      \
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*

# move to dev image
COPY .devcontainer/.tmux.conf /home/user/.tmux.conf

ENV DEBIAN_FRONTEND=dialog

USER user
RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

#
RUN echo "export PS1='🐳  \[\033[1;36m\]\h \[\033[1;34m\]\W\[\033[0;35m\] \[\033[1;36m\]# \[\033[0m\]'" >> /home/user/.bashrc