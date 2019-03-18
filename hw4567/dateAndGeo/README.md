# Helper lib to read / check geo and data values


## 1) install package
```
cd dateAndGeo
```
```
sudo pip3 install -e .
```

## 2) run tests(needs 1)
```
cd dateAndGeo
```
```
python3 -m pytest
```

## 3) run cli(needs 1)
```
cd dateAndGeo
```
```
python3 pylib/cli.py COMMAND ARGUMENT
```
e.g.:

```
python3 pylib/cli.py str2date 'Jun 1 2005  1:33PM'
```
```
python3 pylib/cli.py str2geo '41.5,-81.0'
```

## 4) running tox check
```
cd dateAndGeo
```
```
tox -c tox.ini
```
## 5) checking coverage in pytest
```
python3 -m pytest --cov=dateAndGeo/ dateAndGeo/test/```
```


