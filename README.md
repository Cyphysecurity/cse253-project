# Network Emulation Framework for Industrial Control Systems (NEFICS)

NEFICS aims to provide researchers with a flexible way to simulate high-fidelity devices for industrial control systems.

## Quickstart

Based on Mininet, NEFICS instantiates whichever devices the user specifies within the configuration file used at runtime:

> `python3 -m run conf/simple_powergrid_iec104.json`

## NEFICS runtime

```mermaid
graph LR;
    scenario.json --> run.py;
    run.py --> vNetwork;
    run.py --> vDevice;
    vDevice --> vNetwork;
    vDevice --> launcher.py;
    /modules --> launcher.py;
    launcher.py --> Handler;
    /protos --> Handler;
```

## Sample configuration

The configuration file is in JSON format and specifies the network topology of the simulation, detailing the switches and devices that Mininet will instantiate. A device configuration directive contains its name and DPID. On the other hand, each device has an identifier, network interfaces associated with any corresponding switches, a launcher configuration that determines the process to run within the device, and the network routes.

*conf/simple_powergrid.json:*

```json
{
    "switches": [
        { "name": "s1", "dpid": 1 }
    ],
    "devices": [
        {
            "name": "hsrc",
            "interfaces": [
                {"name": "eth0", "mac": "68:1f:d8:9a:78:1c", "ip": "10.0.1.11/24", "switch": "s1"}
            ],
            "launcher": {
                "module": "simplepowergrid",
                "device": "Source",
                "handler": "RTUHandler",
                "guid": 1, "in": [], "out": [2],
                "parameters": {
                    "voltage": 526315.79
                }
            },
            "routes": [ ["default", "10.0.1.1"] ]
        },
        {
            "name": "htx",
            "interfaces": [
                {"name": "eth0", "mac": "68:1f:d8:76:ac:09", "ip": "10.0.1.12/24", "switch": "s1"}
            ],
            "launcher": {
                "module": "simplepowergrid",
                "device": "Transmission",
                "handler": "RTUHandler",
                "guid": 2, "in": [1], "out": [3],
                "parameters": {
                    "loads": [0.394737, 0.394737, 0.394737],
                    "state": 7
                }
            },
            "routes": [ ["default", "10.0.1.1"] ]
        },
        {
            "name": "hld",
            "interfaces": [
                {"name": "eth0", "mac": "68:1f:d8:bb:a3:f1", "ip": "10.0.1.13/24", "switch": "s1"}
            ],
            "launcher": {
                "module": "simplepowergrid",
                "device": "Load",
                "handler": "RTUHandler",
                "guid": 3, "in": [2], "out": [],
                "parameters": {
                    "load": 12.5
                }
            },
            "routes": [ ["default", "10.0.1.1"] ]
        }
    ]
}
```

## Acknowledgements
This research was possible thanks to the federal grants NIST 70NANB17H282 and DHS/AFRL FA8750-19-2-0010.
