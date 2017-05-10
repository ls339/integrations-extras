# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# stdlib

# 3rd party

# project
from checks import AgentCheck
import psutil
import re
import subprocess

EVENT_TYPE = SOURCE_TYPE_NAME = 'port_monitor'


class Port_monitorCheck(AgentCheck):

    def __init__(self, name, init_config, agentConfig, instances=None):
        AgentCheck.__init__(self, name, init_config, agentConfig, instances)

    def getPortConnectionCount(self, port, conn):
        s = subprocess.check_output(['ss', '-t', '-a', '-n', 'state', 'established'])
        #regex = '.*%s'
        r = re.compile('.*{}'.format(port))
        self.log.debug('regex pattern = %s', r.pattern)
        connection_list = []
        count = 0
        for x in s.split('\n'):
            #connection_list.append(x.split())
            if filter(r.match, x.split()):
                count += 1
        #self.log.debug('count = %s', count)
        return count

    def check(self, instance):
        count = self.getPortConnectionCount(22, 'tcp')
        self.log.debug('count = %d', count)
        self.gauge('port.monitor.tcp', count, tags=['port:22', 'tcp'])
        self.gauge('port.monitor.udp', 10, tags=['port:1276', 'udp'])
        pass

