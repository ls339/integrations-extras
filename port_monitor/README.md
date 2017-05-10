# Port_monitor Integration

## Overview

Get metrics from port_monitor service in real time to:

* Visualize and monitor port_monitor states
* Be notified about port_monitor failovers and events.

## Installation

Install the `dd-check-port_monitor` package manually or with your favorite configuration manager

## Configuration

Edit the `port_monitor.yaml` file to point to your server and port, set the masters to monitor

## Validation

When you run `datadog-agent info` you should see something like the following:

    Checks
    ======

        port_monitor
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The port_monitor check is compatible with all major platforms
