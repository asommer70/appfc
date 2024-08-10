# Publish 

```
pelican content -o output -s publishconf.py                                                                                                
ghp-import -m "Generate Pelican site" --no-jekyll -b master output
git push origin master
```

## Dev

```
pelican -r -l
```

* -l = listen
* -r = autoreload
