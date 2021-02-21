# ###########################################################
# 
# 作成日 2021/02/07     作成者 akihiro.toda
# 更新日 2021/02/07     更新者 akihiro.toda
# 
# Copyright (c) Flugel System Studio - All rights reserved.
# ###########################################################

# ###########################################################
# 
# ベースイメージを指定
# 
# ###########################################################
FROM python:3.9

# ###########################################################
# 
# イメージ作成者
# 
# ###########################################################
LABEL maintainer="akihiro.toda"

# ###########################################################
# 
# パッケージ
# 
# ###########################################################
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install vim

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/