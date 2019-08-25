jobid=$1

sh run_load_file.sh ./conf/conf2/load_file.json_guest_train
sh run_load_file.sh ./conf/conf2/load_file.json_guest_predict
sh run_load_file.sh ./conf/conf2/load_file.json_host_train0
sh run_load_file.sh ./conf/conf2/load_file.json_host_train1
sh run_load_file.sh ./conf/conf2/load_file.json_host_predict0
sh run_load_file.sh ./conf/conf2/load_file.json_host_predict1

 nohup bash run_guest.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2/guest_runtime_conf.json_test $jobid > nohup.guest &
sleep 5
 nohup bash run_host.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2/host_runtime_conf.json_test1 $jobid > nohup.host1 &
nohup bash run_host.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2/host_runtime_conf.json_test0 $jobid> nohup.host0 &

