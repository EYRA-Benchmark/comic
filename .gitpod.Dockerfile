FROM gitpod/workspace-postgres

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
    bash ./Miniconda3-latest-Linux-x86_64.sh -b -p &&\
    rm Miniconda3-latest-Linux-x86_64.sh &&\
    echo . ~/miniconda3/etc/profile.d/conda.sh >> ~/.bashrc &&\
    . ~/miniconda3/etc/profile.d/conda.sh &&\
    conda create -y -n comic python=3 &&\
    echo conda activate comic >> ~/.bashrc &&\
    conda activate comic &&\
    pip install -r requirements.txt &&\ 
    pip install -r requirements.dev.txt &&\
    pip install -e app &&\
    cp .env.dev .env