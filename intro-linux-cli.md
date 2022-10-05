# [Complete intro to linux and the cli](https://btholt.github.io/complete-intro-to-linux-and-the-cli/)

## [Linux](https://btholt.github.io/complete-intro-to-linux-and-the-cli/what-is-linux)

- Linux is unix like, as is macOS, conforms to unix philosophy: programs do one one and only one thing well

  - Linux distribution = distro = something built with the linux kernel
  - Ubuntu is based on Debian, backend by Canonical, a company

- [`$ brew install --cask multipass`](https://multipass.run/docs/installing-on-macos)
  - `multipass launch # create instance`
  - `multipass shell <INSTANCE_NAME>`
  - `multipass list`
- shell (bash, zsh) runs inside of an emulator (iTerm2, Terminal app)

## [Program - Basics](https://btholt.github.io/complete-intro-to-linux-and-the-cli/anatomy-of-a-cli-command)

- `ls --all # -- is long form, only giving 1 flag at a time`
- tack on `--help` to any cli
- bin = binary, all of your runnable programs
- `ls --ignore=snap # = is sometimes required`
- flags are always case sensitive, sometimes order matters
- `cd ~ # home dir`
- `cd / # / means root, root directory of entire project`
- control + R: reverse search, again to search. Left to accept
- `cd # tab 2x to see all possibilities, also for other programs`
- `tail ~/.bash_history # last 10 lines of bash history`
- `!! # run last command`
- `sudo !! # run last command with`

### [Control shortcuts](https://btholt.github.io/complete-intro-to-linux-and-the-cli/signals-and-the-power-of-ctrl)

- CTRL + A – takes you to the beginning of the line
- CTRL + E – takes you to the end of the line
- CTRL + K – "yank" everything after the cursor
- CTRL + U – "yank" everything before the cursor
- CTRL + Y - "paste" (paste in quotes because it doesn't actually go into your system clipboard) everything you yanked
- CTRL + L - clear the screen
- CTRL + R – reverse search through history

### Signal: notification you send to a program

- CTRL + C - SIGINT interrupt
- CTRL + D – SIGQUIT, or `exit`
- SIGTERM - no shortcut, this is what `kill` sends to a program to kill that program
- SKIGKILL - `kill -9` `kill -SIGKILL`, don't cleanup kill ASAP
- `kill -l # see all signals`
- `ps aux | grep name`
- `kill -9 PID`

## [Program - man, tail, head, tar, cat, standard I/O, error](https://btholt.github.io/complete-intro-to-linux-and-the-cli/interacting-with-files)

- [`$ vimtutor`](https://btholt.github.io/complete-intro-to-linux-and-the-cli/vim)
- `less filename # File reading`
- `man less #gets the manual for less, man uses less`
- `cat filename # adds file to standard out, no scroller`
- `tail or head, -n 100 to see first / last of file`
- `tail -f file.txt # tailing the logs realtime`
- `mkdir -p parent/child # makes all folders in path`

Tar

- `tar -zcf archive.tar.gz textfile.txt folder1 # put things into archive and compress it`
- `tar -xzf archive.tar.gz -C destination_folder`

<hr/>

Wild card

- `touch file{1,2}.txt # creates file1.txt, file2.txt, $ touch file-{ca,ny}.txt`
  - Bash actually does this, not touch
- `ls file-* # gets all file- matches, also bash`
- `ls file-??.txt # just 2 matches`

Ranges

- `echo {1..3} # 1, 2, 3`
- `echo {1..5..2} # 1, 3, 5`
- `echo {1..5}{a..z} # 1a, 1b, etc...`

<hr/>

- Unix philosophy, the output of one program could be the input to another. Stream of one piped into another
- `echo 'hello' 1> new-file.txt # 1> just redirect standard out`
- `cat new-file.txt 1>> another-file.txt # appends rather than replaces as with 1>`
- `cat nonexistent-file 2> error.txt # directs standard error`
- `ls > ls.txt # direct both standard out / error `
- `cat file.txt 2> /dev/null # <- this is blackhole, if you don't care about the errors`
- `cat < file.txt # read from file and throw input into cat, which reads it`
- `grep "ls-error.txt" < ls.txt # read from ls.txt, feed to standard in and feed into grep`
- `grep "ls-error.txt" < ls.txt 1> grep.txt 2> /dev/null # see above and feed grep into standard out. Order is not important for this cmd`
- `cat ls.txt | grep "ls-errors.txt"`
- `ps aux | grep "node" # find running node`
- `yes > /dev/null & # & says run this in the background`
- `yes | rm -i file* # yes command to rm which with -i means it will ask for every removal`
- `yes n # n as repeating answer`
- cat reads from standard in, but not echo as echo takes something in and spits it to standard out

<br/>

## [Linux users and permissions](https://btholt.github.io/complete-intro-to-linux-and-the-cli/users-groups-and-permissions)

- linux is a multi user system where programs can be users
- `su # switch user`
- `sudo # switch me into super user then come back`
- `whoami`
- `sudo su # become root`
- Groups: can have privileges, easy for changing a cohort of users
- `sudo usermod -aG sudo brian # add sudo group to brian`
- `-rw-rwx-r- # user, group, everyone else group`
  - Ex. this can be read/written by listed user (first word), rwx by 2nd, etc..
- `chown group:user file# change ownership`
- `chmod u=rw,g=rw,o=rw hello.txt`
- `chmod +x secrets.txt # adds exec to each u,g,o`
- r = 4, w = 3, x = 1
- `sh # login shell, not as powerful as bash`

<br/>

## [Environments & processes](https://btholt.github.io/complete-intro-to-linux-and-the-cli/environments)

- `printenv`
- `USER="Brian" # just for this session`
- `.bash_profile`: only run on login shells
- `.bashrc`: hence, modify this
- **Process**: any command that's currently running
  - will be owned by a user
  - will run in background or foreground (means you can see output)
- `ps aux # without aux, only show current users's procceses`

### Pause and resume process

- `sleep 100`
- control + z to stop
- `jobs # see processes`
- `bg 1 # resume the process in background`
- `fg 1 # reattach to process`
- `sleep 100 > output.txt & # when you run sleep output doesn't get redirected to background `
- If terminal is closed running jobs will be killed
- Use [screen](https://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/) or [tmux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/) to split terminals

### Exit codes, process operators, subcommands

- Exit code: what is returned when a process exits
- `echo $? # last exit code`

| Code | Description                                                                                    |
| ---- | ---------------------------------------------------------------------------------------------- |
| 0    | means it was successful. Anything other than 0 means it failed                                 |
| 1    | a good general catch-all "there was an error"                                                  |
| 2    | a bash internal error, meaning you or the program tried to use bash in an incorrect way        |
| 126  | Either you don't have permission or the file isn't executable                                  |
| 127  | Command not found                                                                              |
| 128  | The exit command itself had a problem, usually that you provided a non-integer exit code to it |
| 130  | Ctrl + C                                                                                       |
| 137  | SIGKILL                                                                                        |
| 255  | Out of bounds, code > 255                                                                      |

- `&&`: run if previous succeeds
- `||`: run if previous fails
- `;`: always run, ex. `false; true; echo hi`
- **Subcommand**: invoke a command within a command
  - ex. `echo I am $(whoami)`
  - ex. `echo hi $(cat < log.txt) user`

<br/>

## [Networking and the internet](https://btholt.github.io/complete-intro-to-linux-and-the-cli/ssh)

- `ssh-keygen -t rsa`
  - Put private key in `~/.ssh`
  - `cat ~/.ssh/id_rsa.pub # copy to clipboard`
- `sftp brian@ip # like ssh but slightly different, auto setup when ssh is`
  - `put file-to-put.txt putted-file.txt # second argument is optional, if you omit it'll just use the same name`
  - `get putted-file.txt gotten-file.txt # same thing, second one is optional`
- `wget https://raw.githubusercontent.com/btholt/bash2048/master/bash2048.sh`
  - Wget is available everywhere, but curl is more feature rich
- `cd ~ && python3 -m http.server 8000 --bind 0.0.0.0`
  - serves files from local system so `localhost:8000/index.html` maps to index.html from home directory
- `curl -X POST http://localhost:8000`: -X to specify verb
- `curl -b "name=brian" http://localhost:8000`: send cookies
- `curl -f cookie_file_name http://localhost:8000`: send cookies
- `curl -L http://bit.ly/linux-cli`: follow redirects
- `curl -H "'accept-language: en-US" -H "Authorization: Bearer 12345" http://localhost:8000`: include headers
- You can right click chrome network request to copy as curl
- `curl <url> | bash`: grab contents of URL of network and pipe directly into bash, only do this for things off GitHub
  - alt. `curl url > file.sh`

<br/>

## [Package management](https://btholt.github.io/complete-intro-to-linux-and-the-cli/what-is-package-management)

- use apt over apt-get
- ex. `sudo apt install lolcat`

```bash
sudo apt autoremove # will remove unused dependencies
sudo apt update # updates the list of available packages apt uses
apt list # everything installed
apt list --upgradable # everything with an update available
sudo apt upgrade # updates all your packages to their latest available versions
sudo apt full-upgrade # basically autoremove and upgrade together
```

- How linux programs are packaged
- [Snap](https://btholt.github.io/complete-intro-to-linux-and-the-cli/snaps): a solution to securely install untrusted code
  - auto updates
  - snap safer than apt
  - snap are sandboxed, cannot break out of home folder

```bash
snap help

sudo apt remove lolcat
sudo snap install lolcat
ls -lsah lolcat

sudo apt remove nodejs
snap info node
sudo snap install --channel=14/stable --classic node
# restart your shell by exiting and starting a new shell
node -e "console.log('hi')"
# classic is trusting the provider of the snap
```

<br/>

## [Writing Your Own Scripts](https://btholt.github.io/complete-intro-to-linux-and-the-cli/writing-your-own-scripts)

- `#! /bin/bash` <- must be in very first line of script, lets bash know how to execute this file
- `#! /usr/bin/python3` from `which python3`
  - then you wouldn't need to do `python3 file`, you can `./file` as in the file it states python3 should be used to run this file
- `#! /snap/bin/node` from `which node`
  - `./nodefile` can run like this
  - we need to ./ to signal that the file is in a root directory, it's not an installed program
- **PATH**: series of location where programs live
- Below, adds bin, which can be another name say "my_bin" to executable

```bash
cd ~
mkdir bin
mv gen_files.sh bin/gen_files
PATH=~/bin:$PATH # : is key so the path is not overwritten
echo $PATH
gen_files
```

- Now we can execute files like they are programs, `$ gen_files`

```bash
# gen_files, usage $ gen_files folder_to_create_in
#! /bin/bash

# $1 is the first argument provided
DESTINATION=$1 # does have to be no spaces to assign
read -p "enter a file prefix: " FILE_PREFIX # FILE_PREFIX doesn't have to be screaming case

# [] translate to test commands so this is $ test -z $DESTINATION, i.e. try $ man test, test returns 0 or 1
# -z means empty string
if [ -z $DESTINATION ]; then
  echo "no path provided, defaulting to ~/temp"
  DESTINATION=~/temp
fi

mkdir -p $DESTINATION
cd $DESTINATION
touch ${FILE_PREFIX}{1..10}.txt # {} is needed here for touch
# {} means get a variable, () means sub command
echo done
```

Else and elif

```bash
if [ $1 -gt 10 ]; then
  echo "greater than 10"
elif [ $1 -lt 10 ]; then
  echo "less than 10"
else
  echo "equals 10"
fi
```

Arrays and for loops

```bash
#!/bin/bash

friends=(Kyle Marc Jem "Brian Holt" Sarah) # note "" not needed unless to capture space

echo My second friend is ${friends[1]}

for friend in ${friends[*]}
do
    echo friend: $friend
done

echo "I have ${#friends[*]} friends"
```

While

```bash
#! /bin/bash
# (( )) converts to let so you can do basic arithmetic, other % won't work
# let "NUM_TO_GUESS = ${RANDOM} % 10 + 1"
NUM_TO_GUESS=$(( $RANDOM % 10 + 1 ))
GUESSED_NUM=0

echo "guess a number between 1 and 10"

while [ $NUM_TO_GUESS -ne $GUESSED_NUM ]
do
  read -p "your guess: " GUESSED_NUM
done

echo "you got it!"
```

<br/>

## [Automation and Customization](https://btholt.github.io/complete-intro-to-linux-and-the-cli/cron)

- jobs = cron jobs, run at some interval
- For Ubuntu you can add scripts to /etc/cron.daily, /etc/cron.weekly to run at intervals
- For another interval, add a file say new_job and put in bin
  - `crontab -u ubuntu -e # runs this as ubuntu user`
  - `* * * * * <command to run> # min, hour, day month, month, day week`
  - `5 * * * * /home/ubuntu/my_bin/make_new_file` every 5 minutes
  - `0/30 * * * 0 cmd` every half hour on sundays, / is what it's divisible by
    - `@reboot` # also works, run on every reboot
    - `@daily`
- [cron to human understandable](https://crontab.guru/)

[Customizations](https://btholt.github.io/complete-intro-to-linux-and-the-cli/customize-your-shell)

- `echo $PS1` shows what your prompt is
- [awesome bash resources](https://github.com/awesome-lists/awesome-bash)
- [symlinks](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/)
