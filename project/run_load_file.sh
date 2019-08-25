conf_path=$1
cur_dir=$(pwd)
load_file_program=$cur_dir/../load_file/load_file.py

python $load_file_program -c $conf_path

