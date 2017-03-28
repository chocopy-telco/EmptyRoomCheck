import redis
import sys


def main():
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        ######################
        # 1. module id
        # 2. status from sensor
        # 3. current time (disconnect check)
        ######################
        r.hmset('1', {'status': '1', 'curr': '134923802342342'})  # set
        r.hmset('2', {'status': '1', 'curr': '134923802342344'})
        r.hmset('3', {'status': '0', 'curr': '134923802342347'})

        print('# HGET')
        print(r.hget('1', 'status'), r.hget('1', 'curr'))  # get
        print(r.hget('2', 'status'), r.hget('2', 'curr'))
        print(r.hget('3', 'status'), r.hget('3', 'curr'))

        print('\n# HMGET')
        print(r.hmget('1', {'curr', 'status'}))  # get
        print(r.hmget('2', {'status', 'curr'}))
        print(r.hmget('3', {'status', 'curr'}))

        if r.hget('1', 'status') == b'1':
            print('\n[1] Room Occupied')
        else:
            print('\n[1] Room Available')

    except Exception as ex:
        print('Error:', ex)
        sys.exit(1)


if __name__ == '__main__':
    main()
