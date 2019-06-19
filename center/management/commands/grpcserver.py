import os
import sys
import time
import concurrent.futures
import signal
import threading
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Thermo center grpc server'

    def __init__(self):
        super().__init__()

        self.stopEvent = threading.Event()

    def shutdown(self, signo, trace):
        self.stopEvent.set()

    def add_arguments(self, parser):
        parser.add_argument('--grpc-port', type=int, default=int(os.environ.get('GRPC_PORT', '8079')),
            help='Grpc Port')
        parser.add_argument('-d', '--daemonize', action='store_true', help='Run in the background')
        parser.add_argument('--configurator', action='store_true', help='Enable Configurator service')
        parser.add_argument('--aggregator', action='store_true', help='Enable Aggregator service')

    def handle(self, *args, **options):
        if options['daemonize']:
            if os.fork() > 0:
                sys.exit()

            os.chdir('/')
            os.setsid()

            if os.fork() > 0:
                sys.exit()

            with open('/dev/null', 'r') as fh:
                os.dup2(fh.fileno(), sys.stdin.fileno())
            with open('/dev/null', 'a+') as fh:
                os.dup2(fh.fileno(), sys.stdout.fileno())
                os.dup2(fh.fileno(), sys.stderr.fileno())

        import grpc

        server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=4), options=(
            ('grpc.keepalive_time_ms', 60000),
            ('grpc.keepalive_timeout_ms', 1000),
            ('grpc.keepalive_permit_without_calls', True),
            ('grpc.http2.max_pings_without_data', 0),
            ('grpc.http2.min_time_between_pings_ms', 10000),
            ('grpc.http2.min_ping_interval_without_data_ms', 1000))
        )

        servicers = []
        if options['configurator']:
            import configurator.daemon
            servicers.append(configurator.daemon.get_servicer())

        if options['aggregator']:
            import aggregator.daemon
            servicers.append(aggregator.daemon.get_servicer())

        if len(servicers) == 0:
            raise RuntimeError('No services enabled')

        for s in servicers:
            s.start(server)

        server.add_insecure_port('0.0.0.0:{}'.format(options['grpc_port']))
        server.start()

        signal.signal(signal.SIGTERM, self.shutdown)

        self.stopEvent.wait()

        server.stop(None).wait()

        for s in servicers:
            s.shutdown()
