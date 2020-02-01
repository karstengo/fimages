# problem

it lists everything of all folders and remembers the listing of everything until app is reloaded and reinitialized.

e.g.

curl http://localhost:5000/testimages

lists content of images/foobar as well if you do that 10 times you have like 100 images on template displayed

```
heyho ['foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages', 'foobar', 'testimages'] 
```

Happens without docker too. 
