## About this project



The collection of salary information on this website that makes it publicly available for anyone to use and share is initially intended to be understood through exploratory analysis of the data and subsequently in an unsupervised analysis to obtain better guidance in relation to what is being offered globally. And gain value with better-informed decisions.




## We need to configure the following items:



- [x] Environment
- [x] Dependencies



---

### Create environment

```
conda create -n yourEnvNameHere python3.9
```

### Update

```
conda update -n base -c defaults conda
```

### To activate this environment, use

```
conda activate yourEnvNameHere
```

###  Install requirements

```
pip install -r requirements.txt
```

###  To deactivate an active environment, use

```
conda deactivate
```

---

### How to get data ?

**make sure you are in your project directory **.

**Run file `get_data.py`**

```
python get_data.py 
```

- **Output**

```
--2023-04-20 13:29:27--  https://ai-jobs.net/salaries/download/salaries.csv
Resolving ai-jobs.net (ai-jobs.net)... 88.99.69.29, 2a01:4f8:10a:154c::2
Connecting to ai-jobs.net (ai-jobs.net)|88.99.69.29|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 218823 (214K) [text/csv]
Saving to: ‘salaries.csv’

salaries.csv                       100%[================================================================>] 213.69K  74.8KB/s    in 2.9s    

2023-04-20 13:29:32 (74.8 KB/s) - ‘salaries.csv’ saved [218823/218823]
```



> When executing above, notice that a new folder with file in the chosen format (csv or json) is created in the current directory.