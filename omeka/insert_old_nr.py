'''

    

'''
import argparse, csv, json, os, re, requests, sys, time, urllib

from queue import Queue
from threading import Thread

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()

class ThreadPool:
    """ Pool of threads consuming tasks from a queue """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()

def main():

    pool = ThreadPool(5)

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    with open (filename) as f:
        datareader = csv.reader(f, delimiter=';', quotechar='"')
        row_count = 0

        for row in datareader:
            row_count += 1
            if row_count % 5 == 0:
                print('Checked '+str(row_count)+' lines.')
                pool.wait_completion()
            
            if(row[0] != 'schema:identifier'):
                ids = row[0].split('|')

                if(len(ids) > 1):
                    pool.add_task(insert_old_nr, ids)
                    

def insert_old_nr(ids):
    with urllib.request.urlopen("https://participatory-archives.ch/api/items?property[0][property]=1632&property[0][type]=eq&property[0][text]="+ids[0]) as url:
        data = json.load(url)[0]

        if(len(data['schema:identifier']) == 1):

            headers = requests.structures.CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Content-Type"] = "application/json"

            url = 'https://participatory-archives.ch/api/items/'+str(data['o:id'])+'?key_identity=7oxjvW9SHAwDSDd3nzFjoe94nC29LBeI&key_credential=ePBflYKBPowsHLaUkNn767jAjZAQBpn0'
            
            data['schema:identifier'].append({
                        'type': 'literal',
                        'property_id': 1632,
                        '@value': ids[1]
                    })

            r = requests.patch(url, data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    main()
