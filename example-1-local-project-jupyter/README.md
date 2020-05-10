# MLPanel - Example 1

Repo Structure
--------------------

    .
    ├── README.md
    ├── config  <- any configuration files
    ├── data    <- source data 
    ├── docker  <- Dockerfile and requirements.txt
    ├── notebooks <- jupyter notebooks with examples and instructions
    ├── docker <- docker image(s) for running project inside container(s)
    ├── docker-compose.yml
    ├── restart.sh <- restart Example docker container
    ├── start.sh   <- start Example docker container
    └── stop.sh    <- stop Example docker container
        

# How to use

### Clone repo

```bash
git clone ...
```

### Create .env

Copy from *.env.template*:

```bash
cp config/.env.template config/.env
```

Edit *config/.env*

### Config & run 

Step-by-step instructions for this example in [MLPanel documentation](https://mlrepa.gitbook.io/mlpanel/tutorials/get-started/examples-with-jupyter-notebook#example-1-local-project-with-jupyter-notebook) 


Start / stop scripts 

```bash
sh start.sh   <- start Example docker container
sh stop.sh    <- stop Example docker container
sh restart.sh <- restart Example docker container

``` 