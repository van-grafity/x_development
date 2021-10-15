add new modul:
create dir models, report, security, views
create file __manifest__.py, __init__.py
and 
DONT FORGET create file ir.model.access.csv

https://www.arsky.id/bagaimana-cara-menginstal-odoo-14-di-ubuntu-18-04/
https://www.candidroot.com/blog/our-candidroot-blog-1/post/how-to-install-odoo-14-on-ubuntu-18-04-66

https://github.com/Marwa-Eltayeb

instal chrome
sudo dpkg -i google-chrome-stable_current_amd64.deb

extract file
tar -zxvf XlsxWriter-1.4.5.tar.gz

edit file
nano /etc/sgeede11-server.conf

create file
touch file1.txt

search file
locate enterprise

all access user change permission folder
sudo chmod -R 777 /namafolder
sudo chmod -R 777 /etc/sgeede11-server.conf

mv odoo11/ /opt/
sudo chmod -R 777 odoo11

permission create file
chmod -R 777 addons/

remove file
rm odoo_14.1alpha1.latest.tar.xz

move file
odoo@ivan-HP-EliteBook-8560p:/opt/opt$ mv odoo-14/ /opt/
or
root@ivan-HP-EliteBook-8560p:/opt/opt# mv odoo-14/ ../

unzip to path folder
unzip file.zip -d destination_folder

zip
sudo zip -r odes_poc_wholesale.zip odes_poc_wholesale/

rename
mv /home/user/oldname /home/user/newname

create user server
sudo su – postgres -c “createuser -s ivan” 2> / dev / null || true

run
ivan@ivan-HP-EliteBook-8560p:/opt/odoo/src$ ./odoo-bin

source recomended
addons/sale/sale.py

wizard
addons/crm/wizard/crm_lead_lost.py
report
odoo11 -> addons -> app_cusrom -> report -> pgs_khs_report_view.xml

server already
kill all server active
pkill -9 python

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==

install requirement
pip3 install -r /opt/odoo/odoo-14/requirements.txt
pip3 install -r requirements.txt

run
./odoo-bin -c /etc/sgeede14-server.conf
or
./odoo-bin

conf (configuration)
multiple path -> addons_path = /opt/odoo11old/addons,/opt/odoo11old/addons_enterprise
/opt/odoo-14$ nano /etc/odoo14-server.conf
or
/opt/odoo-14$ ./odoo-bin -c /etc/odoo14-server.conf

https://www.odoo.com/id_ID/forum/help-1/no-js-argument-is-deprecated-as-inline-javascript-is-disabled-by-default-153851
rename addons_path = /opt/odoo11/addons
edit limit_memory_hard and limit_memory_soft
sudo npm install -g less@3.0.4 less-plugin-clean-css


./odoo-bin -c /etc/sgeede14-server.conf -u ste_custom
./odoo-bin -c /etc/sgeede14-server.conf --dev=all
./odoo-bin -c /etc/sgeede14-server.conf


sudo su postgres
psql <nama database>
jalankan query :

update res_users set  sid = False, exp_date = null, logged_in = False, last_update = null where id = 2;

SVN
svn co svn://svn.sgeede.com/v11/app_custom
sudo -> addons -> svn co svn://svn.sgeede.com/v14/name_modul
svn-st
svn add [PATH]
svn ci -m 'initial commit'
svn up
svn info
svn status
rm -rf .svn

odoo-11
APP_test
we@re$g33d3
 
odoo14 -> user odoo
sudo chmod -R 777 /etc/sgeede11-server.conf
odoo11 -> user ivan
cd /opt/odoo-11/
sudo su odoo -s /bin/bash

POSTGRES

path system
cd /usr/share/postgresql

user permission
nano /etc/postgresql/10/main/pg_hba.conf
sudo service postgresql restart
