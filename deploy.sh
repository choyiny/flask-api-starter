# Start Celery
celery worker -A worker.celery --loglevel=info &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Celery: $status"
  exit $status
fi

# Start Gunicorn on Flask
gunicorn --workers=8 wsgi:application -b 0.0.0.0:5000
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start Flask server: $status"
  exit $status
fi