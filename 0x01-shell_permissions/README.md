This project introduces and tests the knowledge of file permissions in shell script

#0-iam_betty : Switches the current user to betty.
#1-who_am_i: Prints effective name of the cuurent user
#2-groups: The script prints all groups of the current user
#3-new_owner: The script changes the ownner of the file 'hello' to the user 'betty'
#4-empty: The script creates an empty file called hello
#5-execute: The script adds execute permission to the owner of the file hello
#6-multiple_permissions: The script adds execute permission to the owner and the group owner, and read permission of other users, to the file
#7-everybody: The script adds execution permission to the owner, the group owner and the other users, of the file hello
#8-James_Bond: The script sets no permission to the owner and group but sets all permission to other users of the file hello
#9-John_Doe: The script sets the mode of the file hello to -rwxr-x-wx
#10-mirror_permissions: The script sets the mode of the file hello the same as olleh’s mode
#11-directories_permissions: The script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users except regular files
#12-directory_permissions: The script creates a directory called my_dir with permissions 751 in the working directory
#13-change_group: The script changes the group owner to school for the file hello
#100-change_owner_and_group: The script changes all the files and directories in the working directory belonging to owner to vincent, and the group owner to staff
