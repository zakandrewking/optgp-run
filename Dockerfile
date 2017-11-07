FROM dmccloskey/optgpsampler

MAINTAINER Zachary King <zaking17@gmail.com>

USER root

RUN pip install IPython==5.0

WORKDIR $HOME
USER user

CMD ipython
