#!/bin/bash

cd /ExternalHDD5T/GIT/DEVBOX/repositories/
disk_usage1=$(du -s|sed 's/[^0-9]*//g')

echo $disk_usage1

sudo rsync -avp /home/git/repositories/ /ExternalHDD5T/GIT/DEVBOX/repositories/
sudo chown genomels:genomels /ExternalHDD5T/GIT/DEVBOX/repositories/  -R
sudo chmod 775 /ExternalHDD5T/GIT/DEVBOX/repositories/  -R
rsync -avp -e ssh /ExternalHDD5T/GIT/DEVBOX/repositories/  genome@66.170.16.154:/DrSenaPersonalBackup/GIT_US/repositories/

disk_usage2=$(du -s|sed 's/[^0-9]*//g')

echo $disk_usage2

display_date=$(date +%d:%m:%Y)

if ((disk_usage1!=disk_usage2));then    
    diff_val=$((disk_usage2-disk_usage1))
    echo "incremental size:$diff_val K,on $display_date"| mail -s "All GIT Repo synchronized to ExternalHDD (Dev-box)" ganesh.manoharan@genomels.com vinoth.sankaran@genomels.com yuvaram.deepak@genomels.com 
	echo "rsync has increamented files,Mail sent"
else
    echo "No incremental was done,Mail not required"
fi
