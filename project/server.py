import tornado.web
import tornado.httpserver
import tornado.ioloop
import json
import os

from tornado.options import define, options

define("port", default=9052, help="server port", type=int)

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        print("enter server")

    def post(self, *args, **kwargs):
        post_data = json.loads(self.request.body)
        print(post_data)
        msg = {}
        task = post_data["task"]
        msg['userid'] = post_data['userid']
        
        #results = os.listdir("./result")
        #newest_file = results[-1]

        if task == 'binary':
            with open("./result/predict_result_20190825011249.txt") as f:
                for line in f:
                    record = eval(line[:-1].replace("array([", "").replace("])", ""))
                    if record[0] ==  msg['userid']:
                        print("用户ID: ", record[0])
                        msg['理赔概率'] = record[1][1]

                        print("理赔概率: ",  record[1][1])
                        #msg['预测发生理赔'] = record[1][2]

                        print("估计理赔价格", 100 + 150 * record[1][1])      
                        msg["今日健康险价格"] = 100 + 150 * record[1][1]
                          
                        break
        elif task == 'multi':
            with open("./result/predict_result_20190825090903.txt") as f:  
                 for line in f:
                     if line[0] =='(':
                         record = line
                         continue
                     else:
                         record += line
                         record = record.replace('\n', '')
                     record = eval(record.replace("array([", "[").replace("])", "]"))
                     if record[0] == msg['userid']:
                       
                         print(record[1][1])
                         msg['各产品组合推荐概率'] = record[1][1]
                         print(record[1][2])
                         msg['预测产品组合'] = record[1][2]
                         break

        self.finish(msg)
        return

class TaskHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        post_data = json.loads(self.request.body)
        print(post_data)
        task = post_data["task"]
        jobid = post_data['jobid']
        
        if task == 'binary':
            os.system('bash ./run_train_single.sh {}'.format(jobid))
        elif task == 'multi':
            os.system('bash ./run_train_multi.sh {}'.format(jobid))

        msg = {'log_path' :'/data/projects/fate/python/logs/{}'.format(jobid)}
        self.finish(msg)
       
handlers = [(r"/query", QueryHandler), (r'/task', TaskHandler)]

template_path = os.path.join(os.path.dirname(__file__), "template")

if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application(handlers=handlers,
                                  template_path=template_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
