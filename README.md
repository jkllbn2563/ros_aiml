# ros_aiml

### dependence
```
pip install gtts
pip install aiml


```
### text input
```
python aiml_client.py

```
### start the aiml_server
```
python aiml_server.py

```
### start the tts
```
python aiml_tts_client.py

```

### start the stt
```
python robot.py
```
### start the text process and will publish the trigger to the topic /Intent

```
python text_process.py

```
### if you want to change to data of chatbot

```
cd ../data
vim PMC_E.aiml

```
### if you want to use the ros tts
```

git clone https://github.com/ros-drivers/audio_common.git

roscd audio_common
cd sound_play
roslaunch soundplay_node.launch


```







