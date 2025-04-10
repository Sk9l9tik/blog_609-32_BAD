ls articles/templates/articles
for i in $(ls articles/templates/articles/*);
do
cat ${i};
echo '----';
done;

echo '---';
echo 'articles/urls.py:';
cat articles/urls.py;

echo '---';
echo 'articles/views.py:';
cat articles/views.py;


echo '---';
echo 'mysite/urls.py:';
cat mysite/urls.py; 
