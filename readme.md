daily routine
--------------

Install latest python:
```
brew upgrade --all
brew install python freetype pip pyqt zmq
pip install matplotlib numpy ipython pyzmq pygments requests beautifulsoup4 html5lib
```

Launch ipython with inline graphs:

```
ipython qtconsole --pylab=inline
```

Chrome: disable better session restore
```
chrome://flags/
Enable "Disable Better session restore"
```
