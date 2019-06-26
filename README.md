# Web-app
Test project to test a number of technologies:
* various python web libraries such as _Flask_ and _Bottle_,
* Docker and Dockerfiles,
* Google Cloud Build, and
* Google Cloud Run

## Performance
We test the performance of our application in Google Cloud Run.
 To do so, we vary the following parameters:
 * basic `Hello World!`  vs. `Hello World!` with 
 `time.sleep(0.01)`
 * Flask vs. Bottle vs. Bottle with Meinheld
 * Launching with the `gunicorn` command vs. launching with via
 python
 * Modifying the number of threads and workers specified in
 Gunicorn
 
 ### Metrics
 We follow a number of metrics:
 * the number of requests per second
 * the latency of the returned result
 * the memory and processor allocation, representing the
 ability of Google Cloud Run to correctly scale up resources
 
 ### Results
 1. Flask launched with Gunicorn (1 worker, 8 threads)
    1. basic test: high number of requests, very low latency
     (4ms), high container use (40s/s) and increased memory.
    2. sleep test: high number of requests, low latency (8ms),
     high container use (40s/s) and increased memory.
     
 2. Flask launched with python
    1. basic test: high number of requests, very low latency 
     (4ms), high container use (30s/s) and increased memory.
    2. sleep test: low number of requests—one fifth of above
     config—, high latency (300-1000ms), poor container usage 
     (2s/s) and poor memory increase.
 
 3. Bottle launched with python
    1. sleep test: low number of requests (200/s), high 
    latency (1s), low container usage and poor memory increase.
 
 4. Bottle with Meinheld server launched with gunicorn
    1. sleep test, 2 workers: low-to-medium number of requests 
     (200/s), high latency (250-500ms), low container usage 
     (<2s/s) and poor memory increase.
    2. sleep test, 10 workers: high number of requests 
     (500-800/s), low latency (20ms), good container usage 
     (20s/s), good memory scaling.
    3. sleep test, 50 workers: low-medium number of requests 
     (200/s), unreliable latency (20-800ms), average container usage 
     (6s/s), average memory scaling.
    
 ### Summary
 Solutions that do not allow for multi-threading or multiple
 workers struggle when the sleep is introduced. The same can
 be said when the number of threads or workers is too low. It
 seems to be that multi-threading and multiple workers allow
 for a greater memory usage, triggering Google Cloud Run to
 increase resources and hence reduce latency.
 
 In terms of resource efficiency, running a Meinheld server
 through Bottle appears to treat the same number of requests
 using fewer resources (memory and container). However, one
 must be careful not to add too many workers. The Gunicorn
 project makes the following recommendation:
 > Generally we recommend `(2 x $num_cores) + 1` as the number
  of workers to start off with. While not overly scientific, 
  the formula is based on the assumption that for a given core,
  one worker will be reading or writing from the socket while 
  the other worker is processing a request.
 
 