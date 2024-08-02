#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
func: check record timezone is fit files, and find the wrong one.
"""

import argparse
#import logging
import os
import sys


from fit_tool.fit_file import FitFile
from fit_tool.profile.messages.record_message import RecordMessage

from tzfpy import get_tz

def main(args):
    '''
    # logs.
    log_format = '%(asctime)s %(filename)s %(levelname)s %(message)s'
    logger = logging.getLogger()
    log_formatter = logging.Formatter(log_format)
    log_handler = logging.StreamHandler()
    if args.debug:
        log_handler.setLevel(logging.DEBUG)
        #logging.basicConfig(format=log_format, level=logging.DEBUG)
    else:
        log_handler.setLevel(logging.INFO)
        #logging.basicConfig(format=log_format, level=logging.INFO)
    
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)

    logger.info('find fit files.')
    '''
    print('find fit files.')
    fit_dir = os.path.abspath(args.d)
    fit_files = [os.path.join(fit_dir, f) for f in os.listdir(fit_dir) if f.endswith('.fit')]
    if not fit_files:
        #logger.warning('found no fit file, exit.')
        print('found no fit file, exit.')
        sys.exit(0)
    
    #logger.debug('found {} fit files.'.format(len(fit_files)))
    print('found {} fit files.'.format(len(fit_files)))
    
    #logger.info('process fit files.')
    print('process fit files.')
    fit_failed = []
    for fit_file in fit_files:
        #logger.debug('process file {}'.format(fit_file))
        #logger.debug('load file.')
        print('process file {}'.format(fit_file))
        print('load file.')
        sys.stdout.flush()
        fit = FitFile.from_file(fit_file)
        #logger.debug('process records.')
        print('process records.')
        for record in fit.records:
            message = record.message
            if isinstance(message, RecordMessage):
                lat, long = message.position_lat, message.position_long
                timezone = get_tz(long, lat)
                if not timezone:
                    # empty.
                    fit_failed.append(fit_file)
                    break
    
    # output.
    if fit_failed:
        #logger.info('output fit failed file name.')
        print('output fit failed file name.')
        with open(args.o, 'wt') as o:
            o.write('\n'.join(fit_failed) + '\n')
    

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="fit file checker.")
    arg_parser.add_argument('-d', help='fit file directory.', required=True)
    arg_parser.add_argument('-o', help='fit file name with wrong records.', required=True)
    arg_parser.add_argument('--debug', help='debug log mode.', action='store_true', default=False)
    args = arg_parser.parse_args(sys.argv[1:])
    main(args)
