# whisperserver
It uses flask to wrap openai whisper into a http web api server

### how to run it?

just clone the repo and 

    conda create -n whisper python=3.10
    conda activate whisper
    pip install -r requirements.txt
    
if your torch doesn't support cuda, just go to https://pytorch.org/get-started/locally/ and find the one with your system.
for example, if you are running this on ubuntu, use this:

    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



run it with the following command in windows

    start.bat

you can also run this in linux, and it's the same

    flask run --host=0.0.0.0 --port=5500
    
    
### warning, this is only for the purpose of testing, if you need to run this in a production environment, you should
publish flask. the current state is extremely easy to be hacked. check this https://flask.palletsprojects.com/en/2.3.x/deploying/
