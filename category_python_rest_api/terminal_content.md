(base) anshul@anshul:~/code/freelance_projects$ source /home/anshul/anaconda3/bin/activate
(base) anshul@anshul:~/code/freelance_projects$ conda activate anaconda3
Could not find conda environment: anaconda3
You can list all discoverable environments with `conda info --envs`.

(base) anshul@anshul:~/code/freelance_projects$ cd category_python_rest_api/
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git add .
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git commit -am "Configred vagrant and hello world script."
[category_python_rest_api 3c3ca80] Configred vagrant and hello world script.
 1 file changed, 1 insertion(+)
 create mode 100644 category_python_rest_api/hello_world.py
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git push origin
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 381 bytes | 381.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Anshul-GH/freelance_projects.git
   3e5f07a..3c3ca80  category_python_rest_api -> category_python_rest_api
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git add .
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git commit -am "Created django project and app."
[category_python_rest_api 5c0a30d] Created django project and app.
 13 files changed, 200 insertions(+)
 create mode 100755 category_python_rest_api/manage.py
 create mode 100644 category_python_rest_api/profiles_api/__init__.py
 create mode 100644 category_python_rest_api/profiles_api/admin.py
 create mode 100644 category_python_rest_api/profiles_api/apps.py
 create mode 100644 category_python_rest_api/profiles_api/migrations/__init__.py
 create mode 100644 category_python_rest_api/profiles_api/models.py
 create mode 100644 category_python_rest_api/profiles_api/tests.py
 create mode 100644 category_python_rest_api/profiles_api/views.py
 create mode 100644 category_python_rest_api/profiles_project/__init__.py
 create mode 100644 category_python_rest_api/profiles_project/settings.py
 create mode 100644 category_python_rest_api/profiles_project/urls.py
 create mode 100644 category_python_rest_api/profiles_project/wsgi.py
 create mode 100644 category_python_rest_api/requirements.txt
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git push origin
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 4 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (16/16), 3.57 KiB | 730.00 KiB/s, done.
Total 16 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Anshul-GH/freelance_projects.git
   3c3ca80..5c0a30d  category_python_rest_api -> category_python_rest_api
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git add .
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git commit -am "Added custom user profile model, manager, migrations."
[category_python_rest_api c22031b] Added custom user profile model, manager, migrations.
 3 files changed, 89 insertions(+), 1 deletion(-)
 create mode 100644 category_python_rest_api/profiles_api/migrations/0001_initial.py
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git push origin
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 4 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.93 KiB | 986.00 KiB/s, done.
Total 9 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To https://github.com/Anshul-GH/freelance_projects.git
   5c0a30d..c22031b  category_python_rest_api -> category_python_rest_api
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git add .
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git commit -am "Enable django admin for user profile model."
[category_python_rest_api 3d69b6a] Enable django admin for user profile model.
 2 files changed, 3 insertions(+), 2 deletions(-)
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ git push origin
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 572 bytes | 286.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/Anshul-GH/freelance_projects.git
   c22031b..3d69b6a  category_python_rest_api -> category_python_rest_api
(base) anshul@anshul:~/code/freelance_projects/category_python_rest_api$ 