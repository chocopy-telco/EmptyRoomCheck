#!/usr/bin/env python3
import redis
import sys


def main():
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        ######################
        # 1. module id
        # 2. value from sensor
        # 3. current time (disconnect check)
        ######################
        r.hmset('1', {'value': '99', 'curr': '134923802342342'})  # insert
        r.hmset('2', {'value': '1', 'curr': '134923802342344'})
        r.hmset('3', {'value': '292', 'curr': '134923802342347'})

        print('# HGET')
        print(r.hget('1', 'value'), r.hget('1', 'curr'))  # select
        print(r.hget('2', 'value'), r.hget('2', 'curr'))
        print(r.hget('3', 'value'), r.hget('3', 'curr'))

        print('# HMGET')
        print(r.hmget('1', {'curr', 'value'}))  # select
        print(r.hmget('2', {'value', 'curr'}))
        print(r.hmget('2', {'value', 'curr'}))

    except Exception as ex:
        print('Error:', ex)
        sys.exit(1)


if __name__ == '__main__':
    main()
