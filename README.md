# Coppice Finder

## Getting started

1. Download the Ordnance Survey [OpenData Place Names CSV](https://osdatahub.os.uk/downloads/open/OpenNames)

2. Extract the CSV files to the root of this project.

3. Set up a virtualenv:

```
python3 -mvenv env
env/bin/pip install -r requirements.txt
```

4. Generate the map:

```
env/bin/python make.py
```

5. Open `index.html` in a browser to view the map.

## Changes

Issues or PRs welcome, especially ones to update the `names` list in `make.py`
