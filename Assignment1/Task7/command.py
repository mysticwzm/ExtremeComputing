hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1250553/ex1/matrixLarge.txt -output /user/s1413178/data/output/task_7.out -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -numReduceTasks 1