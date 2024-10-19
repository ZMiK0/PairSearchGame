# PairSearchGame

This python game, created for a class project, involves finding pairs of matching symbols. You can compete against another player or against the computer (CPU). If the symbols match, they stay face-up; otherwise, they flip back. The game ends when you find (((rows * columns) / 2) / 2) pairs. It’s a fun game to practice memory skills and enjoy with friends.

All the documentation and project was made by me.


# Installation (Linux Only)


```shell
git clone https://github.com/ZMiK0/PairSearchGame.git
cd PairSearchGame
mv main.py main
chmod a+x main
cd ..
cp -r PairSearchGame ~/.local/bin/
ln -s ~/.local/bin/PairSearchGame/main ~/.local/bin/pairSearchGame
rm -r PairSearchGame
```

## Uninstall
```shell
rm ~/.local/bin/quetask
rm -r ~/.local/bin/PairSearchGame
```

# Use
```shell
$ pairSearchGame
```