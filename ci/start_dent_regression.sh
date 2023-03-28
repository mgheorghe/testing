#!/bin/bash

while [ $# -gt 0 ]; do
  case "$1" in
    --dent=*)
      DENT_BUILD="${1#*=}"
      ;;
    --clean=*)
      CLEAN="${1#*=}"
      ;;
    *)
      printf "***************************\n"
      printf "* Error: Invalid argument.*\n"
      printf "***************************\n"
      exit 1
  esac
  shift
done

RUN_DATE=`date +"%d-%m-%Y-%H-%M-%S"` 

echo "DENT_BUILD = ${DENT_BUILD}"
echo "RUN_DATE   = ${RUN_DATE}"         

echo 'check if another run is already in progress'
echo 'IMPLEMENT ME'

rm -rf ./testing

git clone https://github.com/dentproject/testing.git

echo 'build the dent framework container if there is a need for it'
DENT_CONTAINER_TAG=$(sha1sum "./testing/DentOS_Framework/Dockerfile" | cut -d ' ' -f 1)
docker image ls dent/test-framework | grep $DENT_CONTAINER_TAG &> /dev/null
if [ $? -ne 0 ]; then
    echo "could not find any container with TAG=$DENT_CONTAINER_TAG"
    echo "building the dent/test-framework:$DENT_CONTAINER_TAG container"
    docker build --no-cache --tag dent/test-framework:latest ./testing/DentOS_Framework
    docker tag dent/test-framework:latest dent/test-framework:$DENT_CONTAINER_TAG
fi


echo 'split container in 2 base and dent framework'
echo 'IMPLEMENT ME'

echo 'install onie build dent image ....'
echo 'IMPLEMENT ME'

echo 'start ixnetwork container'
virsh shutdown IxNetwork-930
sleep 10
virsh start IxNetwork-930
sleep 120
echo 'IMPLEMENT ME'

echo 'creating log folders'
LOG_DIR="/home/dent/logs/$DENT_BUILD-$RUN_DATE"
mkdir -p ${LOG_DIR}
echo "logs can be found in ${LOG_DIR}"

echo 'run dent os cleanup'
docker run --rm --network host \
        --name suite_group_clean_config_$RUN_DATE \
        --mount src=$LOG_DIR,target=/dent-fw/reports,type=bind \
        --mount src=$LOG_DIR,target=/dent-fw/logs,type=bind \
        -d dent/test-framework:$DENT_CONTAINER_TAG dentos_testbed_runtests \
        -d --stdout \
        --config ./DentOsTestbed/configuration/testbed_config/sit/testbed.json \
        --config-dir ./DentOsTestbed/configuration/testbed_config/sit/ \
        --suite-groups suite_group_clean_config \
        --discovery-reports-dir ./reports

echo 'wait for run to end'
docker wait suite_group_clean_config_$RUN_DATE


echo 'run dent os amazon test cases'
docker run --rm --network host \
        --name dentos_testbed_runtests_$RUN_DATE \
        --mount src=$LOG_DIR,target=/dent-fw/reports,type=bind \
        --mount src=$LOG_DIR,target=/dent-fw/logs,type=bind \
        -d dent/test-framework:$DENT_CONTAINER_TAG dentos_testbed_runtests \
        -d --stdout \
        --config ./DentOsTestbed/configuration/testbed_config/sit/testbed.json \
        --config-dir ./DentOsTestbed/configuration/testbed_config/sit/ \
        --suite-groups \
            suite_group_test \
            suite_group_l3_tests \
            suite_group_basic_trigger_tests \
            suite_group_traffic_tests \
            suite_group_tc_tests \
            suite_group_bgp_tests \
            suite_group_system_wide_testing \
            suite_group_system_health \
            suite_group_store_bringup \
            suite_group_alpha_lab_testing \
            suite_group_dentv2_testing \
            suite_group_connection \
            suite_group_platform \
        --discovery-reports-dir DISCOVERY_REPORTS_DIR \
        --discovery-reports-dir ./reports \
        --discovery-path ./DentOsTestbedLib/src/dent_os_testbed/discovery/modules/

echo 'wait for run to end'
docker wait dentos_testbed_runtests_$RUN_DATE

echo 'run dent os marvell test cases'
echo 'IMPLEMENT ME'



echo 'redirect all the output to a file for history purposes'
echo 'IMPLEMENT ME'