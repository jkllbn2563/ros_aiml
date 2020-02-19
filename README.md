# ros_aiml

### dependence
```
pip install gtts
pip install aiml
pip install PyAudio
```
### text input
```
python aiml_client.py

```
### start the aiml_server, the google tts,and the text process
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
### start the text process and will publish the trigger to the topic /Intent,and the newest version is merged to the aiml_server.py

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
### keyword:STATION B publish:IntentFind
```
<li> Ok, I will send it to the station B,and the current state is IntentFind </li>
<li> Sure, let's do this,and the current state is IntentFind </li>
<li> No preblem, I am going to do it,and the current state is IntentFind </li>
```
### keyword:REPOSITORY publish:IntentDelivery
```
<li> OK, I will deliver them to the repository,and the current state is IntentDelivery </li>
<li> OK, Sure, let's do this,and the current state is IntentDelivery </li>
<li> No preblem, I am going to deliver them,and the current state is IntentDelivery </li>


```
### keyword: HOME publish:IntentHome
```
<li> OK, I will go home right now,and the current state is IntentHome </li>
<li> OK, Sure, let's go home,and the current state is IntentHome </li>
<li> No preblem, I am on my way home,and the current state is IntentHome </li>
```
### keyword: follow publish:IntentFollow
```
<li> OK, I will follow you right now,and the current state is IntentFollow </li>
<li> No preblem, I will follow your step,and the current state is IntentFollow </li>
!! just say "follow me" :Where are we going?
```

### keyword: _ WHAT HAPPENED publish:IntentWhat
```
start the image caption
```
### other
```
What are you doing?
What time is it?
where are you from?


