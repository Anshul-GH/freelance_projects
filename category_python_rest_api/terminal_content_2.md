(base) anshul@anshul:~/code/freelance_projects$ cd category_python_rest_api/
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'ubuntu/bionic64' version '20200304.0.0' is up to date...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 8000 (guest) => 8000 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.42
    default: VirtualBox Version: 6.1
==> default: Mounting shared folders...
    default: /vagrant => /home/anshul/code/freelance_projects/category_python_rest_api
==> default: Running provisioner: shell...
    default: Running: inline script
    default: Removed /etc/systemd/system/timers.target.wants/apt-daily.timer.
    default: Hit:1 http://archive.ubuntu.com/ubuntu bionic InRelease
    default: Get:2 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
    default: Get:3 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
    default: Get:4 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
    default: Get:5 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages [8570 kB]
    default: Get:6 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [1784 kB]
    default: Get:7 http://archive.ubuntu.com/ubuntu bionic/universe Translation-en [4941 kB]
    default: Get:8 http://archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages [151 kB]
    default: Get:9 http://archive.ubuntu.com/ubuntu bionic/multiverse Translation-en [108 kB]
    default: Get:10 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [2132 kB]
    default: Get:11 http://archive.ubuntu.com/ubuntu bionic-updates/main Translation-en [422 kB]
    default: Get:12 http://archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [389 kB]
    default: Get:13 http://archive.ubuntu.com/ubuntu bionic-updates/restricted Translation-en [52.8 kB]
    default: Get:14 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1739 kB]
    default: Get:15 http://security.ubuntu.com/ubuntu bionic-security/main Translation-en [329 kB]
    default: Get:16 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages [365 kB]
    default: Get:17 http://archive.ubuntu.com/ubuntu bionic-updates/universe Translation-en [371 kB]
    default: Get:18 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [26.6 kB]
    default: Get:19 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse Translation-en [6792 B]
    default: Get:20 http://archive.ubuntu.com/ubuntu bionic-backports/main amd64 Packages [10.0 kB]
    default: Get:21 http://archive.ubuntu.com/ubuntu bionic-backports/main Translation-en [4764 B]
    default: Get:22 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [10.3 kB]
    default: Get:23 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [4588 B]
    default: Get:24 http://security.ubuntu.com/ubuntu bionic-security/restricted Translation-en [48.9 kB]
    default: Get:25 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [1130 kB]
    default: Get:26 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [256 kB]
    default: Get:27 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages [19.2 kB]
    default: Get:28 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [4412 B]
    default: Fetched 23.1 MB in 8s (2898 kB/s)
    default: Reading package lists...
    default: Reading package lists...
    default: Building dependency tree...
    default: Reading state information...
    default: The following additional packages will be installed:
    default:   python-pip-whl python3-distutils python3-lib2to3 python3.6-venv unzip
    default: The following NEW packages will be installed:
    default:   python-pip-whl python3-distutils python3-lib2to3 python3-venv python3.6-venv
    default:   unzip zip
    default: 0 upgraded, 7 newly installed, 0 to remove and 6 not upgraded.
    default: Need to get 2217 kB of archives.
    default: After this operation, 6249 kB of additional disk space will be used.
    default: Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python-pip-whl all 9.0.1-2.3~ubuntu1.18.04.5 [1653 kB]
    default: Get:2 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 python3-lib2to3 all 3.6.9-1~18.04 [77.4 kB]
    default: Get:3 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 python3-distutils all 3.6.9-1~18.04 [144 kB]
    default: Get:4 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3.6-venv amd64 3.6.9-1~18.04ubuntu1.4 [6188 B]
    default: Get:5 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3-venv amd64 3.6.7-1~18.04 [1208 B]
    default: Get:6 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 unzip amd64 6.0-21ubuntu1.1 [168 kB]
    default: Get:7 http://archive.ubuntu.com/ubuntu bionic/main amd64 zip amd64 3.0-11build1 [167 kB]
    default: dpkg-preconfigure: unable to re-open stdin: No such file or directory
    default: Fetched 2217 kB in 1s (1537 kB/s)
    default: Selecting previously unselected package python-pip-whl.
(Reading database ... 60028 files and directories currently installed.)
    default: Preparing to unpack .../0-python-pip-whl_9.0.1-2.3~ubuntu1.18.04.5_all.deb ...
    default: Unpacking python-pip-whl (9.0.1-2.3~ubuntu1.18.04.5) ...
    default: Selecting previously unselected package python3-lib2to3.
    default: Preparing to unpack .../1-python3-lib2to3_3.6.9-1~18.04_all.deb ...
    default: Unpacking python3-lib2to3 (3.6.9-1~18.04) ...
    default: Selecting previously unselected package python3-distutils.
    default: Preparing to unpack .../2-python3-distutils_3.6.9-1~18.04_all.deb ...
    default: Unpacking python3-distutils (3.6.9-1~18.04) ...
    default: Selecting previously unselected package python3.6-venv.
    default: Preparing to unpack .../3-python3.6-venv_3.6.9-1~18.04ubuntu1.4_amd64.deb ...
    default: Unpacking python3.6-venv (3.6.9-1~18.04ubuntu1.4) ...
    default: Selecting previously unselected package python3-venv.
    default: Preparing to unpack .../4-python3-venv_3.6.7-1~18.04_amd64.deb ...
    default: Unpacking python3-venv (3.6.7-1~18.04) ...
    default: Selecting previously unselected package unzip.
    default: Preparing to unpack .../5-unzip_6.0-21ubuntu1.1_amd64.deb ...
    default: Unpacking unzip (6.0-21ubuntu1.1) ...
    default: Selecting previously unselected package zip.
    default: Preparing to unpack .../6-zip_3.0-11build1_amd64.deb ...
    default: Unpacking zip (3.0-11build1) ...
    default: Setting up python-pip-whl (9.0.1-2.3~ubuntu1.18.04.5) ...
    default: Setting up unzip (6.0-21ubuntu1.1) ...
    default: Setting up python3.6-venv (3.6.9-1~18.04ubuntu1.4) ...
    default: Setting up zip (3.0-11build1) ...
    default: Setting up python3-lib2to3 (3.6.9-1~18.04) ...
    default: Setting up python3-distutils (3.6.9-1~18.04) ...
    default: Setting up python3-venv (3.6.7-1~18.04) ...
    default: Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    default: Processing triggers for mime-support (3.60ubuntu1) ...
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ vagrant ssh
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-147-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Jul 16 18:39:34 UTC 2021

  System load:  0.18              Processes:             106
  Usage of /:   3.1% of 38.71GB   Users logged in:       0
  Memory usage: 14%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%


5 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '20.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


vagrant@ubuntu-bionic:~$ exit
logout
Connection to 127.0.0.1 closed.
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ vagrant ssh
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-147-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Jul 16 18:58:17 UTC 2021

  System load:  0.08              Processes:             98
  Usage of /:   3.1% of 38.71GB   Users logged in:       0
  Memory usage: 14%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%


5 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '20.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Fri Jul 16 18:39:35 2021 from 10.0.2.2
vagrant@ubuntu-bionic:~$ cd /vagrant
vagrant@ubuntu-bionic:/vagrant$ touch test.txt
vagrant@ubuntu-bionic:/vagrant$ ls
README.md  Vagrantfile  default_Vagrantfile  test.txt  ubuntu-bionic-18.04-cloudimg-console.log  vagrant_log.md
vagrant@ubuntu-bionic:/vagrant$ ls
README.md  Vagrantfile  default_Vagrantfile  ubuntu-bionic-18.04-cloudimg-console.log  vagrant_log.md
vagrant@ubuntu-bionic:/vagrant$ ls 
README.md  Vagrantfile  default_Vagrantfile  hello_world.py  ubuntu-bionic-18.04-cloudimg-console.log  vagrant_log.md
vagrant@ubuntu-bionic:/vagrant$ python hello_world.py
Hello World!!
vagrant@ubuntu-bionic:/vagrant$ python -m venv ~/env
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ deactivate
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ pip install -r requirements.txt
Collecting django==2.2 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/54/85/0bef63668fb170888c1a2970ec897d4528d6072f32dee27653381a332642/Django-2.2-py3-none-any.whl (7.4MB)
    100% |████████████████████████████████| 7.5MB 131kB/s 
Collecting djangorestframework==3.9.2 (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/cc/6d/5f225f18d7978d8753c1861368efc62470947003c7f9f9a5cc425fc0689b/djangorestframework-3.9.2-py2.py3-none-any.whl (911kB)
    100% |████████████████████████████████| 921kB 616kB/s 
Collecting pytz (from django==2.2->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/70/94/784178ca5dd892a98f113cdd923372024dc04b8d40abe77ca76b5fb90ca6/pytz-2021.1-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 1.1MB/s 
Collecting sqlparse (from django==2.2->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/14/05/6e8eb62ca685b10e34051a80d7ea94b7137369d8c0be5c3b9d9b6e3f5dae/sqlparse-0.4.1-py3-none-any.whl (42kB)
    100% |████████████████████████████████| 51kB 2.4MB/s 
Installing collected packages: pytz, sqlparse, django, djangorestframework
Successfully installed django-2.2 djangorestframework-3.9.2 pytz-2021.1 sqlparse-0.4.1
(env) vagrant@ubuntu-bionic:/vagrant$ django-admin.py startproject profiles_project .
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 19 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, authtoken, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

July 16, 2021 - 19:10:48
Django version 2.2, using settings 'profiles_project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
[16/Jul/2021 19:11:05] "GET / HTTP/1.1" 200 16348
[16/Jul/2021 19:11:05] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[16/Jul/2021 19:11:05] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[16/Jul/2021 19:11:05] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[16/Jul/2021 19:11:05] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
Not Found: /favicon.ico
[16/Jul/2021 19:11:05] "GET /favicon.ico HTTP/1.1" 404 1982
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py makemigrations profiles_api
Migrations for 'profiles_api':
  profiles_api/migrations/0001_initial.py
    - Create model UserProfile
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, profiles_api, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying profiles_api.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying sessions.0001_initial... OK
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py createsuperuser
Email: qwerty@asdf.com
Name: GildroY
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/home/vagrant/env/lib/python3.6/site-packages/django/core/management/__init__.py", line 381, in execute_from_command_line
    utility.execute()
  File "/home/vagrant/env/lib/python3.6/site-packages/django/core/management/__init__.py", line 375, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/vagrant/env/lib/python3.6/site-packages/django/core/management/base.py", line 323, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/vagrant/env/lib/python3.6/site-packages/django/contrib/auth/management/commands/createsuperuser.py", line 61, in execute
    return super().execute(*args, **options)
  File "/home/vagrant/env/lib/python3.6/site-packages/django/core/management/base.py", line 364, in execute
    output = self.handle(*args, **options)
  File "/home/vagrant/env/lib/python3.6/site-packages/django/contrib/auth/management/commands/createsuperuser.py", line 156, in handle
    self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)
  File "/vagrant/profiles_api/models.py", line 25, in create_superuser
    user = self._create_user(email, name, password)
AttributeError: 'UserProfileManager' object has no attribute '_create_user'
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py createsuperuser
Email: qwerty@asdf.com
Name: GildroY
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 16, 2021 - 19:51:00
Django version 2.2, using settings 'profiles_project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
[16/Jul/2021 19:51:13] "GET / HTTP/1.1" 200 16348
[16/Jul/2021 19:51:13] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[16/Jul/2021 19:51:13] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[16/Jul/2021 19:51:13] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[16/Jul/2021 19:51:13] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
[16/Jul/2021 19:51:26] "GET /admin HTTP/1.1" 301 0
[16/Jul/2021 19:51:26] "GET /admin/ HTTP/1.1" 302 0
[16/Jul/2021 19:51:26] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1816
[16/Jul/2021 19:51:27] "GET /static/admin/css/base.css HTTP/1.1" 200 16378
[16/Jul/2021 19:51:27] "GET /static/admin/css/login.css HTTP/1.1" 200 1233
[16/Jul/2021 19:51:27] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17944
[16/Jul/2021 19:51:39] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[16/Jul/2021 19:51:39] "GET /admin/ HTTP/1.1" 200 4066
[16/Jul/2021 19:51:39] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[16/Jul/2021 19:51:39] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 412
[16/Jul/2021 19:51:39] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[16/Jul/2021 19:52:51] "GET /admin/profiles_api/userprofile/ HTTP/1.1" 200 4428
[16/Jul/2021 19:52:51] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6170
[16/Jul/2021 19:52:51] "GET /static/admin/js/core.js HTTP/1.1" 200 7135
[16/Jul/2021 19:52:51] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 363
[16/Jul/2021 19:52:51] "GET /static/admin/js/urlify.js HTTP/1.1" 200 8972
[16/Jul/2021 19:52:51] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 6918
[16/Jul/2021 19:52:51] "GET /admin/jsi18n/ HTTP/1.1" 200 3223
[16/Jul/2021 19:52:51] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1530
[16/Jul/2021 19:52:51] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 128820
[16/Jul/2021 19:52:52] "GET /static/admin/js/actions.js HTTP/1.1" 200 6538
[16/Jul/2021 19:52:52] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 271751
[16/Jul/2021 19:52:52] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[16/Jul/2021 19:52:57] "GET /admin/profiles_api/userprofile/1/change/ HTTP/1.1" 200 11308
[16/Jul/2021 19:52:57] "GET /static/admin/css/forms.css HTTP/1.1" 200 8518
[16/Jul/2021 19:52:57] "GET /static/admin/css/widgets.css HTTP/1.1" 200 10340
[16/Jul/2021 19:52:57] "GET /static/admin/js/calendar.js HTTP/1.1" 200 7777
[16/Jul/2021 19:52:57] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 20274
[16/Jul/2021 19:52:57] "GET /static/admin/js/change_form.js HTTP/1.1" 200 712
[16/Jul/2021 19:52:57] "GET /admin/jsi18n/ HTTP/1.1" 200 3223
[16/Jul/2021 19:52:57] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 495
[16/Jul/2021 19:52:57] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
[16/Jul/2021 19:52:57] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
(env) vagrant@ubuntu-bionic:/vagrant$ 