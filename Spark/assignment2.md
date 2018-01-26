
In this weeks assignments you will join and aggregate data from a collection of user and restaurant in Mexico. The collections we use is from: https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data

We have placed three files in the folder of this tutorial: 
- `userprofile.csv`: describes several atributes of the users
- `geoplaces2.csv`:  describes several attributes of the restaurants
- `rating_final.csv`: describes how the users rated the restaurant, the food and the service on a scale [0-2]

## part 1 ##

The first assignment is to estimate whether people with a larger budget are generally more satisfied with the restaurant they choose.

Create an RDD `rating` of the restaurant rating (the first rating) in `rating_final.csv`.


```python
ratings_final = sc.textFile("rating_final.csv")
firstline = ratings_final.first()
ratings_finalNoHeader = ratings_final.filter(lambda x: x != firstline)
ratingsSplit = ratings_finalNoHeader.map(lambda x: x.split(','))
rating = ratingsSplit.map(lambda x: (x[0], x[1], x[2] ) ) 
rating.take(5)
```




    [('U1077', '135085', '2'),
     ('U1077', '135038', '2'),
     ('U1077', '132825', '2'),
     ('U1077', '135060', '1'),
     ('U1068', '135104', '1')]



Also create an RDD `userbudget` in which you load the `userID` and `budget` from `userprofiles.csv`.


```python
user_profile_final = sc.textFile("userprofile.csv")
firstline = user_profile_final.first()
user_profile_final_NoHeader = user_profile_final.filter(lambda x: x != firstline)
user_profile_Split = user_profile_final_NoHeader.map(lambda x: x.split(','))
user_profile_Split.take(5)
userbudget = user_profile_Split.map(lambda x: (x[0], x[17]) ) 
userbudget.take(5)
```




    [('U1001', 'medium'),
     ('U1002', 'low'),
     ('U1003', 'low'),
     ('U1004', 'medium'),
     ('U1005', 'medium')]



To join the `userbudget` with the `userrating`, you must convert the `ratings` to a (userID, rating) structure (we don't need the placeID for this assignment).


```python
firstlineFilter = rating.first()
ratings_final_Final = rating.filter(lambda x: x != firstlineFilter)
useratings = ratings_final_Final.map(lambda x: (x[0], x[2]))
useratings.take(5)
```




    [('U1077', '2'),
     ('U1077', '2'),
     ('U1077', '2'),
     ('U1077', '1'),
     ('U1068', '1')]



Join `useratings` and `userbudget`, and map the result to a `(budget, rating)` structure. Don't forget to convert rating to an int (with `int()`).


```python
users_union = userbudget.leftOuterJoin(useratings) 
union_convert = users_union.map(lambda x:  (x[1][0], int(x[1][1]) ) )
union_convert.take(5)

```




    [('low', 1), ('low', 1), ('low', 2), ('low', 1), ('low', 1)]



Group the result by budget (the key), and compute the average rating. To compute the average of a list `l` in python you can divide `sum(l)` by `len(l)`.


```python
budget_group = union_convert.aggregateByKey(\
                  0, # initial value for an accumulator \
                  lambda r, v: (r + v) / 2 , # function that adds a value to an accumulator \
                  lambda r1, r2: (r1 + r2) / 2 # function that merges/combines two accumulators \
                 )
budget_group.collect()

budget_group_other = union_convert.aggregateByKey(\
                  0, # initial value for an accumulator \
                  lambda r, v: (r + v) / 1 , # function that adds a value to an accumulator \
                  lambda r1, r2: (r1 + r2) / 1 # function that merges/combines two accumulators \
                 )

budget_group_other.collect()

final = budget_group_other.map(lambda x:  (x[0], x[1] / (union_convert.filter(lambda y: y[0] == x[0] )).count()      ) )
final.collect()
```

    Traceback (most recent call last):
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 148, in dump
        return Pickler.dump(self, obj)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 409, in dump
        self.save(obj)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 751, in save_tuple
        save(element)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 255, in save_function
        self.save_function_tuple(obj)
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 292, in save_function_tuple
        save((code, closure, base_globals))
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 736, in save_tuple
        save(element)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 781, in save_list
        self._batch_appends(obj)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 805, in _batch_appends
        save(x)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 255, in save_function
        self.save_function_tuple(obj)
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 292, in save_function_tuple
        save((code, closure, base_globals))
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 736, in save_tuple
        save(element)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 781, in save_list
        self._batch_appends(obj)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 808, in _batch_appends
        save(tmp[0])
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 249, in save_function
        self.save_function_tuple(obj)
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py", line 297, in save_function_tuple
        save(f_globals)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 476, in save
        f(self, obj) # Call unbound method with explicit self
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 821, in save_dict
        self._batch_setitems(obj.items())
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 852, in _batch_setitems
        save(v)
      File "/opt/jupyterhub/anaconda/lib/python3.6/pickle.py", line 496, in save
        rv = reduce(self.proto)
      File "/opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py", line 204, in __getnewargs__
        "It appears that you are attempting to broadcast an RDD or reference an RDD from an "
    Exception: It appears that you are attempting to broadcast an RDD or reference an RDD from an action or transformation. RDD transformations and actions can only be invoked by the driver, not inside of other transformations; for example, rdd1.map(lambda x: rdd2.values.count() * x) is invalid because the values transformation and count action cannot be performed inside of the rdd1.map transformation. For more information, see SPARK-5063.



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in dump(self, obj)
        147         try:
    --> 148             return Pickler.dump(self, obj)
        149         except RuntimeError as e:


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in dump(self, obj)
        408             self.framer.start_framing()
    --> 409         self.save(obj)
        410         self.write(STOP)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_tuple(self, obj)
        750         for element in obj:
    --> 751             save(element)
        752 


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function(self, obj, name)
        254             if klass is None or klass is not obj:
    --> 255                 self.save_function_tuple(obj)
        256                 return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function_tuple(self, func)
        291         save(_make_skel_func)
    --> 292         save((code, closure, base_globals))
        293         write(pickle.REDUCE)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_tuple(self, obj)
        735             for element in obj:
    --> 736                 save(element)
        737             # Subtle.  Same as in the big comment below.


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_list(self, obj)
        780         self.memoize(obj)
    --> 781         self._batch_appends(obj)
        782 


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in _batch_appends(self, items)
        804                 for x in tmp:
    --> 805                     save(x)
        806                 write(APPENDS)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function(self, obj, name)
        254             if klass is None or klass is not obj:
    --> 255                 self.save_function_tuple(obj)
        256                 return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function_tuple(self, func)
        291         save(_make_skel_func)
    --> 292         save((code, closure, base_globals))
        293         write(pickle.REDUCE)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_tuple(self, obj)
        735             for element in obj:
    --> 736                 save(element)
        737             # Subtle.  Same as in the big comment below.


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_list(self, obj)
        780         self.memoize(obj)
    --> 781         self._batch_appends(obj)
        782 


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in _batch_appends(self, items)
        807             elif n:
    --> 808                 save(tmp[0])
        809                 write(APPEND)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function(self, obj, name)
        248             #print("save global", islambda(obj), obj.__code__.co_filename, modname, themodule)
    --> 249             self.save_function_tuple(obj)
        250             return


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in save_function_tuple(self, func)
        296         # save the rest of the func data needed by _fill_function
    --> 297         save(f_globals)
        298         save(defaults)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        475         if f is not None:
    --> 476             f(self, obj) # Call unbound method with explicit self
        477             return


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save_dict(self, obj)
        820         self.memoize(obj)
    --> 821         self._batch_setitems(obj.items())
        822 


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in _batch_setitems(self, items)
        851                 save(k)
    --> 852                 save(v)
        853                 write(SETITEM)


    /opt/jupyterhub/anaconda/lib/python3.6/pickle.py in save(self, obj, save_persistent_id)
        495             if reduce is not None:
    --> 496                 rv = reduce(self.proto)
        497             else:


    /opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py in __getnewargs__(self)
        203         raise Exception(
    --> 204             "It appears that you are attempting to broadcast an RDD or reference an RDD from an "
        205             "action or transformation. RDD transformations and actions can only be invoked by the "


    Exception: It appears that you are attempting to broadcast an RDD or reference an RDD from an action or transformation. RDD transformations and actions can only be invoked by the driver, not inside of other transformations; for example, rdd1.map(lambda x: rdd2.values.count() * x) is invalid because the values transformation and count action cannot be performed inside of the rdd1.map transformation. For more information, see SPARK-5063.

    
    During handling of the above exception, another exception occurred:


    PicklingError                             Traceback (most recent call last)

    <ipython-input-60-866a8920f24c> in <module>()
         13 
         14 final = budget_group_other.map(lambda x:  (x[0], x[1] / (union_convert.filter(lambda y: y[0] == x[0] )).count()      ) )
    ---> 15 final.collect()
    

    /opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py in collect(self)
        807         """
        808         with SCCallSiteSync(self.context) as css:
    --> 809             port = self.ctx._jvm.PythonRDD.collectAndServe(self._jrdd.rdd())
        810         return list(_load_from_socket(port, self._jrdd_deserializer))
        811 


    /opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py in _jrdd(self)
       2453 
       2454         wrapped_func = _wrap_function(self.ctx, self.func, self._prev_jrdd_deserializer,
    -> 2455                                       self._jrdd_deserializer, profiler)
       2456         python_rdd = self.ctx._jvm.PythonRDD(self._prev_jrdd.rdd(), wrapped_func,
       2457                                              self.preservesPartitioning)


    /opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py in _wrap_function(sc, func, deserializer, serializer, profiler)
       2386     assert serializer, "serializer should not be empty"
       2387     command = (func, profiler, deserializer, serializer)
    -> 2388     pickled_command, broadcast_vars, env, includes = _prepare_for_python_RDD(sc, command)
       2389     return sc._jvm.PythonFunction(bytearray(pickled_command), env, includes, sc.pythonExec,
       2390                                   sc.pythonVer, broadcast_vars, sc._javaAccumulator)


    /opt/jupyterhub/spark-2.2.0/python/pyspark/rdd.py in _prepare_for_python_RDD(sc, command)
       2372     # the serialized command will be compressed by broadcast
       2373     ser = CloudPickleSerializer()
    -> 2374     pickled_command = ser.dumps(command)
       2375     if len(pickled_command) > (1 << 20):  # 1M
       2376         # The broadcast will have same life cycle as created PythonRDD


    /opt/jupyterhub/spark-2.2.0/python/pyspark/serializers.py in dumps(self, obj)
        458 
        459     def dumps(self, obj):
    --> 460         return cloudpickle.dumps(obj, 2)
        461 
        462 


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in dumps(obj, protocol)
        702 
        703     cp = CloudPickler(file,protocol)
    --> 704     cp.dump(obj)
        705 
        706     return file.getvalue()


    /opt/jupyterhub/spark-2.2.0/python/pyspark/cloudpickle.py in dump(self, obj)
        160                 msg = "Could not serialize object: %s: %s" % (e.__class__.__name__, emsg)
        161             print_exec(sys.stderr)
    --> 162             raise pickle.PicklingError(msg)
        163 
        164     def save_memoryview(self, obj):


    PicklingError: Could not serialize object: Exception: It appears that you are attempting to broadcast an RDD or reference an RDD from an action or transformation. RDD transformations and actions can only be invoked by the driver, not inside of other transformations; for example, rdd1.map(lambda x: rdd2.values.count() * x) is invalid because the values transformation and count action cannot be performed inside of the rdd1.map transformation. For more information, see SPARK-5063.


Indeed, it seems that users with a higher budget are more satisfied with the restaurants they visit.

## Part 2 ##

The next assignment is to estimate whether users ratings are affected by the distance between where they live and where the restaurant is. 

We want to compute the distance between the user's home and the restaurant for every rating. Both positions can be looked up from the userprofiles and the places.

Create an RDD `userpos` with the userID, latitude and longitude from `userprofiles.csv`. To use the location, put latitude and longitude inside a tuple.


```python
user_profile_final = sc.textFile("userprofile.csv")
user_profile_final.take(5)
```




    ['userID,latitude,longitude,smoker,drink_level,dress_preference,ambience,transport,marital_status,hijos,birth_year,interest,personality,religion,activity,color,weight,budget,height',
     'U1001,22.139997,-100.978803,false,abstemious,informal,family,on foot,single,independent,1989,variety,thrifty-protector,none,student,black,69,medium,1.77',
     'U1002,22.150087,-100.983325,false,abstemious,informal,family,public,single,independent,1990,technology,hunter-ostentatious,Catholic,student,red,40,low,1.87',
     'U1003,22.119847,-100.946527,false,social drinker,formal,family,public,single,independent,1989,none,hard-worker,Catholic,student,blue,60,low,1.69',
     'U1004,18.867,-99.183,false,abstemious,informal,family,public,single,independent,1940,variety,hard-worker,none,professional,green,44,medium,1.53']



Create a broadcast variable that contains a dictionary from which you can lookup a users position based on their ID.


```python

```

Also create an RDD `placepos` that contains the ID and position of places in `geoplaces2.csv`.


```python

```

And create a similar broadcast variable to lookup the position of a place based in it's ID.


```python

```

To compute the distance an accurate approximation is the Vincenty distance in the geopy library (use `pip install geopy` to install). 

Here is an example to compute the distance:


```python
from geopy.distance import vincenty
vincenty((31.8300167,35.0662833), (31.83,35.0708167)).meters
```

Now, map the ratings, so that you retrieve the position of the user and the position of the restaurant, and compute the vincenti distance between them. Output the distance and rating.


```python

```

Now average the distance per rating.


```python

```

It seems that there is no linear relation between the distance to the restaurant and the given rating.
