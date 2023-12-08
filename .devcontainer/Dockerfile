FROM python:3.12

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
RUN pip install --upgrade pip

CMD ["bash"]
