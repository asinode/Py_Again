#!/bin/bash
cd  /ExternalHDD5T/GIT/DEVBOX/repositories/
disk_usage1=$(du -s|sed 's/[^0-9]*//g')

rsync -avp -e ssh genome@66.170.16.154:/DrSenaPersonalBackup/GIT_US/repositories/  /ExternalHDD5T/GIT/DEVBOX/repositories/
sudo  rsync -avp /ExternalHDD5T/GIT/DEVBOX/repositories/  /home/git/repositories/

disk_usage2=$(du -s|sed 's/[^0-9]*//g')

echo $disk_usage2

display_date=$(date +%d:%m:%Y)

if ((disk_usage1!=disk_usage2));then
    diff_val=$((disk_usage2-disk_usage1))
    echo "incremental size:$diff_val K,on $display_date"| mail -s "GNA Repo synchronized to ExternalHDD (Dev-Box)" tamilvanan.periyasamy@genomels.com #ganesh.manoharan@genomels.com vinoth.sankaran@genomels.com yuvaram.deepak@genomels.com
    echo "rsync has increamented files,Mail sent"
else
    echo "No incremental was done,Mail not required"
fi

