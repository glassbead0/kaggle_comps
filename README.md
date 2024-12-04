## Kaggle Competitions

#### Titanic

(Do the following steps in a VS code terminal if desired)
* `cd ~/workspace/kaggle`
* `docker/build_image.sh`
* `docker/run_container.sh`
* (from in the container) `docker/start_jupyter.sh`
* you can ctrl+c and the jupyter server will continue running on port 8888

### In VS Code

* ensure Jupyter extension is installed
* open a notebook, select kernel (existing Jupyter server)
* type `http://localhost:8888`


### Jupyter console in kernal for current notebook

* make sure you're running the docker container and started Jupyter in VS code terminal
* open the notebook you want to work on
* from in the docker container in VS code, type `jupyter console --existing`
* you will likely need to exit the jupyter console and start a new one if you switch notebooks.

## Troubleshooting ideas

* restart VS code
* restart jupyter server (requires reconnecting to the server in VS code)
* restart docker container