hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1250553/ex2/task2/logsLarge.txt -output /user/s1413178/data/output/assignment2/task3.2.1 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py
hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1413178/data/output/assignment2/task3.2.1 -output /user/s1413178/data/output/assignment2/task3.2 -mapper mapperTop10.py -file mapperTop10.py -reducer reducerTop10.py -file reducerTop10.py -numReduceTasks 1