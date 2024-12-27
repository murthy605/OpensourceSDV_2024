"""
 * Copyright(c) 2021 ZettaScale Technology and others
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License v. 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0, or the Eclipse Distribution License
 * v. 1.0 which is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * SPDX-License-Identifier: EPL-2.0 OR BSD-3-Clause
"""

import time
import random
import os
from cyclonedds.core import Qos, Policy
from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import Publisher, DataWriter
from cyclonedds.topic import Topic
from cyclonedds.util import duration

from vehicles import Vehicle


# This is the publisher in the Vehicle Demo. It publishes a randomly moving
# vehicle updated every 0.1-1.0 seconds randomly. The 'Vehicle' class was
# generated from the vehicle.idl file with `idlc -l py vehicle.idl`
#os.environ['CYCLONEDDS_URI'] = 'Default_test.xml'

qos = Qos(
    Policy.Reliability.Reliable(duration(microseconds=60)),
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.TransientLocal,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant()
#domain_participant.transport_config = "UDP/192.168.178.12"
domain_participant.transport_config = (
    "UDP/192.168.178.12"  # Bind to specific interface
    "?multicastRecvAddress=239.255.0.1"  # Multicast receive address
    "&multicastSendAddress=239.255.0.1"  # Multicast send address
)
domain_participant.interface_address = "192.168.178.12"  # Replace with your machine's IP address
domain_participant.port = 7400  # You can set a specific port for your application
topic = Topic(domain_participant, 'Vehicle', Vehicle, qos=qos)
publisher = Publisher(domain_participant)
writer = DataWriter(publisher, topic)


vehicle = Vehicle(name="Dallara IL-15", x=200, y=200)


while True:
    vehicle.x += random.choice([-1, 0, 1])
    vehicle.y += random.choice([-1, 0, 1])
    writer.write(vehicle)
    print(">> Wrote vehicle")
    time.sleep(random.random() * 0.9 + 0.1)
