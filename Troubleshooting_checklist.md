# Approaches to troubleshooting in bioinformatics – A checklist 

When a command is not working, you are getting an unexpected output, etc, it might help you to go through this list to solve the issue!

## Common issues

+ Are you in the right folder / directory? ('mapp' in Swedish) (use `pwd`)
+ Is your input file in the right folder or are you providing the right path to it? (use `ls`)
+ Is your input file what it should be? E.g. is the format correct? (use `less`)
+ Double check the command - any typo in the name of the software, of the files etc, will make it impossible for the command to be executed.
+ If -Y forwarding is not working on Solander: maybe you connected with `ssh -Y` from an existing Solander session. In that case log out completely from Solander and try again.
+ To interrupt a process: press 'Ctrl' and 'C'.
+ Try to read the error message. Sometimes they are not very informative, but sometimes they are!

## Useful commands:

+ `pwd`
+ `cd`
+ `less` (exit with 'q')
+ `cat`
+ `nano`
+ `cp from_folder/filename to_folder/filename` If you want to copy entire folders, use `cp -r`. If you are in 'to_folder' already and you want the same filename, you can use `cp from_folder/filename .` .

## Transfer files between your computer and Solander

Open a new terminal window. Navigate to the folder where you want to work (i.e. either the folder containing the files you want to transfer to Solander, or the folder where you want to copy the files currently on Solander).

Log in to Solander with the `sftp` protocol instead of `ssh`: `sftp your_user_name@solander.ibg.uu.se`

Navigate to the right folder using `cd`.

If you need to navigate on your own computer, use `lcd` (or `lpwd` to know where you are).

To copy files FROM your computer TO Solander: use `put` and the name of the file.

To copy files FROM Solander TO your computer: use `get` and the name of the file.

If you wish to copy entire folders, use the `-r` flag.

