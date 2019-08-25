jobid=$1

sh run_load_file.sh ./conf/conf2-multitarget/load_file.json_guest_predict
sh run_load_file.sh ./conf/conf2-multitarget/load_file.json_host_predict0
sh run_load_file.sh ./conf/conf2-multitarget/load_file.json_host_predict1

 nohup bash run_guest.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2-multitarget/guest_runtime_conf.json_predict $jobid > nohup.guest &
sleep 5
 nohup bash run_host.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2-multitarget/host_runtime_conf.json_predict1 $jobid > nohup.host1 &
nohup bash run_host.sh /data/projects/fate/python/examples/hetero_secureboosting_tree/conf/conf2-multitarget/host_runtime_conf.json_predict0 $jobid> nohup.host0 &

