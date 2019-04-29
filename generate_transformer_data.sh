#!/bin/bash
mkdir -p $HOME/t2t_data /tmp/t2t_datagen
t2t-datagen --t2t_usr_dir=./transformer --data_dir=$HOME/t2t_data --tmp_dir=/tmp/t2t_datagen --problem=code_transformer