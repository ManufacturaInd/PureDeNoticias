# PureDeNoticias

## Notas de instalação:

As várias dependências podem ser instaladas num só comando:

    pip install -r requirements.txt

No Debian, surge um erro relacionado com a package `cffi`; precisamos de instalar a development package da `libffi`:

    sudo aptitude install libffi-dev

## Chaves de autorização do Twitter

Não está incluído no repo o ficheiro com as chaves de autorização do Twitter (naturalmente). Para isto funcionar, é preciso ter um ficheiro de texto `keys.txt` na raiz do projeto, estruturado da seguinte forma:

    <consumer key>
    <consumer secret>
    <access key>
    <access secret>
