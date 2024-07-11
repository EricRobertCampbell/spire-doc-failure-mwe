FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    libicu-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY Spire.Doc-12.6.0-py3-none-manylinux1_x86_64.whl /tmp/Spire.Doc-12.6.0-py3-none-manylinux1_x86_64.whl

RUN pip3 install /tmp/Spire.Doc-12.6.0-py3-none-manylinux1_x86_64.whl --break-system-packages && \
    rm /tmp/Spire.Doc-12.6.0-py3-none-manylinux1_x86_64.whl

COPY test.py /usr/src/app/

WORKDIR /usr/src/app

CMD ["python3", "test.py"]
