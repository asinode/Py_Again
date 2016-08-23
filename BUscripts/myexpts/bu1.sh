#!/bin/bash
####################################
#
# Backup to NFS mount script.
#
####################################
#sudo chown -R genomels:genomels /var/www/html/glstimesheet/mysqldump
#sudo chown -R genomels:genomels /home/git
#sudo chmod 774 /var/www/html/glstimesheet/mysqldump /home/git -R

# What to backup..(select multiple path)  
backup_files="/home/gitolite-admin /home/git  /mysqldump from US NGS MACHINE"

# Where to backup to.

#dest="/data2/backup"
dest="/data2/backup"
# Create archive filename.
day=$(date +%d-%b-%y-%a)
#day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

#sudo rsync -ab --backup-dir=`date +%F_%T` --delete --exclude=old_* /home/gitolite-admin /home/git /data2/backup/autoback_weekly 
sudo rsync -ab  --delete  /home/gitolite-admin /home/git /data2/backup/autoback_weekly   /data2/backup/cronjob


#status=$?

sudo tar czvPf $dest/$archive_file  /data2/backup/cronjob

#Warning
#Error
#Alert


# Backup the files using tar.

#tar zcfP$dest /$archive_file $backup_files
#tar cfP $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls $dest
#ls $backup_files
	
