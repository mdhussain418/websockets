### Python 3.x.x required. Tested on 3.8.1 python version
# install websocket and websocket-client with below commands before starting the process
# pip install websocket
# pip install websocket-client

# install ssl with below command if want to disable cert check if using self signed certificates.
# pip install ssl

import websocket
import ssl
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # tried with python 3.8    
    header = {"Authorization" : "Basic QVFBQUFBRndPdHl4TGdBQUEtbkFfTEsxOmFiY2RzYXM="}
    ws = websocket.WebSocketApp("wss://echo.websocket.org", header = header,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    # without proxy
    ws.run_forever()

    
    # with proxy
    # http_proxy_host=None, http_proxy_port=None,
    # ws.run_forever(http_proxy_host = 'proxy host', http_proxy_port = 'proxy port')


    # disable ssl cert verification
    # this helps when working with self signed certificates.
    # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False})
