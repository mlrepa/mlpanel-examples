# MLPanel - Example 3


Repo Structure
--------------------

    .
    ├── README.md
    ├── config          <- any configuration files
    ├── data   
    │   ├── processed   <- data after all preprocessing has been done
    │   └── raw         <- original unmodified data acting as source of truth and provenance
    ├── docker          <- Dockerfile and requirements.txt
    ├── experiments     <- local temp folder to store experiment results 
    │   └── models      <- local temp model storage
    ├── notebooks       <- jupyter notebooks with examples and instructions
    ├── src
    │   ├── data        <- .py modules to prepare and process data prepare
    │   ├── pipelines   <- scripts to run Example pipelines (train / evaluate) 
    │   ├── report      <- visualization
    │   ├── train       <- train model .py modules
    │   └── utils.py    <- utils functions
    ├── README.md
    ├── restart.sh <- restart Example docker container
    ├── start.sh   <- start Example docker container
    └── stop.sh    <- stop Example docker container
     

# How to use

### Clone repo

```bash
git clone ...
```

### Put Google Application credentials

1. [generate credentials json](https://console.cloud.google.com/apis/credentials/serviceaccountkey);
2. select json type;
3. save it into folder *config/* 

### Create .env

Copy from *.env.template*:

```bash
cp config/.env.template config/.env
```

Edit *config/.env*

### Config & run 

Step-by-step instructions for this example in [MLPanel documentation](https://mlrepa.gitbook.io/mlpanel/tutorials/get-started/examples-with-jupyter-notebook#example-3-deploy-model-as-web-service-with-gcp-tbd) 


Start / stop scripts 

```bash
sh start.sh   <- start Example docker container
sh stop.sh    <- stop Example docker container
sh restart.sh <- restart Example docker container

``` 